from threading import Thread
import socket
import sys
import select
import queue
import json
from pymongo import MongoClient
import loguru
import schedule
from time import sleep


class room_socket():
    def __init__(self, collection, ip, port, limit=10):
        self.room_logger = loguru.logger
        self.db_collection = collection
        self.room_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.room_ip = ip

        self.room_port = port

        self.room_socket.bind((self.room_ip, self.room_port))
        self.room_logger.info("Binding successful!")
        self.room_logger.info(f"Base server bound to: {self.room_ip}:{self.room_port}")

        self.room_socket.listen(limit)
        self.inputs = [self.room_socket]
        self.outputs = []
        self.message_queues = {}
        self.room_logger.info(f"Base server limit set at {limit}")
        self.message_queues["all"] = queue.Queue()

    def close(self):
        self.room_socket.close()

    def log_online_users(self):
        self.room_logger.info(f"users online: {len(self.inputs)-1}|  {self.inputs[1:]}")

    def cleanup(self):
        self.room_logger.debug("checking activity")
        if len(self.inputs) == 1:
            self.room_logger.info("room empty, unmaking")
            self.inputs.pop(self.room_socket)
            return

    def presence(self):
        timeout = 5
        closing = []
        self.room_logger.debug("sending presences")
        for check_socket in self.inputs:
            if check_socket is not self.room_socket:
                presence_message = {"OPS": "presence"}
                try:
                    check_socket.send(json.dumps(presence_message).encode("UTF-8"))
                    data = check_socket.recv(1024)
                except ConnectionError:
                    closing.append(check_socket)
                    continue
                while not data:
                    if timeout == 0:
                        closing.append(check_socket)
                    sleep(1)
                    timeout -= 1
                decoded_data = json.loads(data.decode("UTF-8"))
                if decoded_data.get("response", None) == "here":
                    continue
                else:
                    closing.append(check_socket)
        for closing_socket in closing:
            self.inputs.remove(closing_socket)

    def send_data(self, s):
        self.room_logger.debug(f"sending message to {s.getpeername()}")
        try:
            next_msg = self.message_queues[s.getpeername()].get_nowait()
            if next_msg.get("at_user") == "all":
                next_msg = self.message_queues["all"].get_nowait()
                for connection in self.inputs:
                    if connection != self.room_socket:
                        self.room_logger.debug(f"sent to {s}")
                        connection.send(json.dumps(next_msg).encode("UTF-8"))
            else:
                for connection in self.inputs:
                    if connection != self.room_socket:
                        if connection.getpeername() == next_msg.get("at_user"):
                            self.room_logger.debug(f"sent to {s}")
                            connection.send(json.dumps(next_msg).encode("UTF-8"))
        except queue.Empty:
            # No messages waiting so stop checking for writability.
            self.room_logger.warning(f"socket {s.getpeername()} queue empty")
            self.outputs.remove(s)
        except OSError:
            # No messages waiting so stop checking for writability.
            self.room_logger.warning(f"socket {s.getpeername()} probably disconnected")
            self.outputs.remove(s)

    def recieve_data(self, s):
        if s is self.room_socket:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            connection.setblocking(0)
            self.inputs.append(connection)
            self.room_logger.info(f"new connection {connection.getpeername()}")

            # Give the connection a queue for data we want to send
            self.message_queues[connection.getpeername()] = queue.Queue()
        else:
            try:
                data = s.recv(1024)
            except ConnectionResetError:
                self.room_logger.info(f"user {s.getpeername()} quit")
                del self.message_queues[s.getpeername()]
                self.inputs.remove(s)
                self.room_logger.debug(f"user {s.getpeername()} queue deleted")
                self.room_logger.debug(f"socket {s.getpeername()} closed")
            try:
                decoded_data = json.loads(data.decode("UTF-8"))
                self.room_logger.info(f"recieved message from {s.getpeername()}, {decoded_data}")
                operation = decoded_data.get("OPS", None)
                if not operation:
                    error_response = json.dumps(({"error": "no operation specified"}))
                    s.send(error_response.encode("UTF-8"))
                if operation == "QUIT":
                    self.room_logger.info(f"user {s.getpeername()} quit")
                elif operation == "MESSAGE":
                    at_user = decoded_data.get("at_user", None)
                    if not at_user:
                        error_response = json.dumps(({"error": "sent to noone"}))
                        s.send(error_response.encode("UTF-8"))
                    if at_user == "all":
                        for user in self.message_queues.keys():
                            self.message_queues["all"].put(decoded_data)
                            self.room_logger.debug(f"queue for {at_user} {self.message_queues[user].queue}")
                    else:
                        # A readable client socket has data
                        self.message_queues[at_user].put(decoded_data)
                    # Add output channel for response
                    if s not in self.outputs:
                        self.outputs.append(s)
            except json.decoder.JSONDecodeError:
                self.room_logger.info(f"malformed message recieved from {connection.getpeername()}")
                error_response = json.dumps(({"error": "malformed"}))
                s.send(error_response.encode("UTF-8"))
            except UnboundLocalError:
                pass

    def room_loop(self):
        schedule.every(5).minutes.do(self.log_online_users)
        schedule.every(5).minutes.do(self.presence)
        schedule.every(5).minutes.do(self.cleanup)
        while self.inputs:
            schedule.run_pending()
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
            # Handle inputs
            for s in readable:
                self.recieve_data(s)
            # TODO figure out that weird queue block error
            # Handle outputs
            for s in writable:
                self.send_data(s)

            # Handle "exceptional conditions"
            for s in exceptional:
                # Stop listening for input on the connection
                self.inputs.remove(s)
                if s in self.outputs:
                    self.outputs.remove(s)
                s.close()

                # Remove message queue
                del self.message_queues[s.getpeername()]
            sleep(0.2)
        self.room_logger.info(f"room {self.room_port} closing")


class room_server():
    def __init__(self, ip=None, limit=10, port=6661):
        self.base_logger = loguru.logger
        self.client = MongoClient('127.0.0.1:27017')

        self.db = self.client['chat_apps']
        self.collection = self.db['client-server']

        self.base_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not ip:
            self.base_host_name = socket.gethostname()
            self.base_ip = socket.gethostbyname(self.base_host_name)
        else:
            self.base_ip = ip

        self.base_port = port

        self.base_socket.bind((self.base_ip, self.base_port))
        self.base_logger.info("Binding successful!")
        self.base_logger.info(f"Base server bound to: {self.base_ip}:{self.base_port}")

        self.base_socket.listen(limit)
        self.base_logger.info(f"Base server limit set at {limit}")
        self.rooms = []

    def room_service(self):
        self.base_logger.debug("main loop started")
        while True:
            try:
                conn, add = self.base_socket.accept()

                self.base_logger.info(f"Received connection from {conn.getpeername()}")
                self.base_logger.info(f'Connection Established. Connected From: {conn.getpeername()}')
                greeting_data = json.loads((conn.recv(1024)).decode("UTF-8"))
                if not greeting_data.get('username') or not greeting_data.get("target_room"):
                    error_response = json.dumps(({"status":"error", "message": "data malformed"}))
                    conn.send(error_response.encode("UTF-8"))
                    conn.close()
                    self.base_logger.warning(f"malformed data at {conn}, data: {greeting_data}")
                self.base_logger.info(f'greetings from {greeting_data.get("username")} {greeting_data}')

                location = greeting_data.get("target_room")
                if location == self.base_port:
                    error_response = json.dumps(({"status":"error", "message": "no"}))
                    conn.send(error_response.encode("UTF-8"))
                    conn.close()
                    self.base_logger.warning(f"{conn.getpeername()} tried to override base socket")
                else:
                    room_data = self.collection.find_one({"ROOM": location})
                    self.base_logger.debug(f"queried data for {location}| {room_data}")
                    if not room_data:
                        self.base_logger.debug("no room found, creating")
                        room_response = json.dumps(({"status": "warning", "message": "no room found, opening new"}))
                        conn.send(room_response.encode("UTF-8"))
                        room_thread = Thread(target=self.open_room, args=([location]))
                        room_thread.start()
                        self.rooms.append((room_thread, location))
                        conn.close()
                    else:
                        if conn.getpeername() not in room_data.get("Blacklist"):
                            error_response = json.dumps(({"status": "success", "message": "connection allowed"}))
                            result_of_check = self.base_socket.connect_ex((self.base_ip, location))
                            if result_of_check == 0:  # port open
                                self.base_logger.info(f"allowed user {greeting_data.get('username')} to connect to room {location}")
                            else:
                                self.base_logger.info(f"recreated room {location}")
                                room_thread = Thread(target=self.open_room, args=([location]))
                                room_thread.start()
                                self.rooms.append((room_thread, location))
                            self.base_logger.info(f"allowed user {greeting_data.get('username')} to connect to room {location}")
                            conn.send(error_response.encode("UTF-8"))
                            conn.close()
                        else:
                            error_response = json.dumps(({"status":"error", "message": "no room found"}))
                            conn.send(error_response.encode("UTF-8"))
                            conn.close()
                            self.base_logger.warning("user blacklisted")

            except KeyboardInterrupt:
                try:
                    conn.close()
                    self.base_socket.close()
                    return
                except UnboundLocalError:
                    self.base_socket.close()
                    return
        for room in self.rooms:  # server closed, close all rooms
            room.join()

    def add_room(self, room):
        added_room = self.collection.insert_one({"ROOM": room, "Blacklist": [], "Whitelist": [], "Users": []}).inserted_id
        self.base_logger.info(f"created room records, room № {room}")
        return added_room

    def remove_room(self, room):
        self.collection.delete_one({"ROOM": room})
        self.base_logger.info(f"deleted records, room № {room}")
        return

    def open_room(self, port):
        try:
            room = room_socket(self.collection, self.base_ip, port)
            if not self.collection.find({"ROOM": port}):
                self.base_logger.debug("creating_room")
                self.add_room(port)
            room.room_loop()
            room.close()
            self.base_logger.info(f"room {port} closed")
            # self.remove_room(port)
        except Exception as ex:
            self.base_logger.error(ex)

    def shutdown(self):
        self.base_socket.close()


server = room_server(ip="127.0.0.1")
room_thread = Thread(target=server.room_service, args=())
room_thread.start()
room_thread.join()
