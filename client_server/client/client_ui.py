# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 681, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.username_input = QtWidgets.QLineEdit(self.login_page)
        self.username_input.setGeometry(QtCore.QRect(280, 170, 201, 20))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.login_page)
        self.password_input.setGeometry(QtCore.QRect(280, 210, 201, 20))
        self.password_input.setObjectName("password_input")
        self.username_lable = QtWidgets.QLabel(self.login_page)
        self.username_lable.setGeometry(QtCore.QRect(200, 170, 71, 21))
        self.username_lable.setObjectName("username_lable")
        self.password_lable = QtWidgets.QLabel(self.login_page)
        self.password_lable.setGeometry(QtCore.QRect(200, 210, 47, 13))
        self.password_lable.setObjectName("password_lable")
        self.sign_in_button = QtWidgets.QPushButton(self.login_page)
        self.sign_in_button.setGeometry(QtCore.QRect(200, 280, 75, 23))
        self.sign_in_button.setObjectName("sign_in_button")
        self.register_page_button = QtWidgets.QPushButton(self.login_page)
        self.register_page_button.setGeometry(QtCore.QRect(200, 310, 75, 23))
        self.register_page_button.setObjectName("register_page_button")
        self.port_lable = QtWidgets.QLabel(self.login_page)
        self.port_lable.setGeometry(QtCore.QRect(200, 250, 47, 13))
        self.port_lable.setObjectName("port_lable")
        self.port_input = QtWidgets.QLineEdit(self.login_page)
        self.port_input.setGeometry(QtCore.QRect(280, 250, 201, 20))
        self.port_input.setObjectName("port_input")
        self.stackedWidget.addWidget(self.login_page)
        self.registration_page = QtWidgets.QWidget()
        self.registration_page.setObjectName("registration_page")
        self.about_me_input = QtWidgets.QTextEdit(self.registration_page)
        self.about_me_input.setGeometry(QtCore.QRect(120, 200, 391, 151))
        self.about_me_input.setObjectName("about_me_input")
        self.username_input_reg = QtWidgets.QLineEdit(self.registration_page)
        self.username_input_reg.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.username_input_reg.setObjectName("username_input_reg")
        self.password_input_reg = QtWidgets.QLineEdit(self.registration_page)
        self.password_input_reg.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.password_input_reg.setObjectName("password_input_reg")
        self.username_lable_reg = QtWidgets.QLabel(self.registration_page)
        self.username_lable_reg.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.username_lable_reg.setObjectName("username_lable_reg")
        self.password_lable_reg = QtWidgets.QLabel(self.registration_page)
        self.password_lable_reg.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.password_lable_reg.setObjectName("password_lable_reg")
        self.about_me_lable = QtWidgets.QLabel(self.registration_page)
        self.about_me_lable.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.about_me_lable.setObjectName("about_me_lable")
        self.register_button = QtWidgets.QPushButton(self.registration_page)
        self.register_button.setGeometry(QtCore.QRect(30, 380, 75, 23))
        self.register_button.setObjectName("register_button")
        self.login_page_button = QtWidgets.QPushButton(self.registration_page)
        self.login_page_button.setGeometry(QtCore.QRect(30, 420, 75, 23))
        self.login_page_button.setObjectName("login_page_button")
        self.stackedWidget.addWidget(self.registration_page)
        self.rooms = QtWidgets.QWidget()
        self.rooms.setObjectName("rooms")
        self.connected_rooms = QtWidgets.QTabWidget(self.rooms)
        self.connected_rooms.setGeometry(QtCore.QRect(10, 40, 651, 501))
        self.connected_rooms.setObjectName("connected_rooms")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.message_input_box = QtWidgets.QTextEdit(self.tab)
        self.message_input_box.setGeometry(QtCore.QRect(20, 310, 531, 61))
        self.message_input_box.setObjectName("message_input_box")
        self.user_choice_box = QtWidgets.QComboBox(self.tab)
        self.user_choice_box.setGeometry(QtCore.QRect(280, 390, 69, 22))
        self.user_choice_box.setObjectName("user_choice_box")
        self.status_lable = QtWidgets.QLabel(self.tab)
        self.status_lable.setGeometry(QtCore.QRect(560, 10, 47, 13))
        self.status_lable.setObjectName("status_lable")
        self.status_state_placeholder = QtWidgets.QLabel(self.tab)
        self.status_state_placeholder.setGeometry(QtCore.QRect(560, 30, 71, 16))
        self.status_state_placeholder.setObjectName("status_state_placeholder")
        self.send_to_user_button = QtWidgets.QPushButton(self.tab)
        self.send_to_user_button.setGeometry(QtCore.QRect(140, 390, 121, 23))
        self.send_to_user_button.setObjectName("send_to_user_button")
        self.send_all_button = QtWidgets.QPushButton(self.tab)
        self.send_all_button.setGeometry(QtCore.QRect(20, 390, 75, 23))
        self.send_all_button.setObjectName("send_all_button")
        self.send_quit_message = QtWidgets.QPushButton(self.tab)
        self.send_quit_message.setGeometry(QtCore.QRect(20, 430, 75, 23))
        self.send_quit_message.setObjectName("send_quit_message")
        self.add_from_contacts_button = QtWidgets.QPushButton(self.tab)
        self.add_from_contacts_button.setGeometry(QtCore.QRect(140, 420, 121, 23))
        self.add_from_contacts_button.setObjectName("add_from_contacts_button")
        self.remove_from_contacts_button = QtWidgets.QPushButton(self.tab)
        self.remove_from_contacts_button.setGeometry(QtCore.QRect(140, 450, 121, 23))
        self.remove_from_contacts_button.setObjectName("remove_from_contacts_button")
        self.message_output_box = QtWidgets.QTextBrowser(self.tab)
        self.message_output_box.setGeometry(QtCore.QRect(20, 10, 531, 261))
        self.message_output_box.setObjectName("message_output_box")
        self.connected_rooms.addTab(self.tab, "")
        self.room_manager_button = QtWidgets.QPushButton(self.rooms)
        self.room_manager_button.setGeometry(QtCore.QRect(10, 10, 151, 23))
        self.room_manager_button.setObjectName("room_manager_button")
        self.stackedWidget.addWidget(self.rooms)
        self.room_manager_page = QtWidgets.QWidget()
        self.room_manager_page.setObjectName("room_manager_page")
        self.ping_contacts_button = QtWidgets.QPushButton(self.room_manager_page)
        self.ping_contacts_button.setGeometry(QtCore.QRect(10, 400, 75, 23))
        self.ping_contacts_button.setObjectName("ping_contacts_button")
        self.room_browser_lable = QtWidgets.QLabel(self.room_manager_page)
        self.room_browser_lable.setGeometry(QtCore.QRect(320, 70, 91, 16))
        self.room_browser_lable.setObjectName("room_browser_lable")
        self.current_rooms_lable = QtWidgets.QLabel(self.room_manager_page)
        self.current_rooms_lable.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.current_rooms_lable.setObjectName("current_rooms_lable")
        self.room_number_input = QtWidgets.QLineEdit(self.room_manager_page)
        self.room_number_input.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.room_number_input.setObjectName("room_number_input")
        self.connect_to_room_button = QtWidgets.QPushButton(self.room_manager_page)
        self.connect_to_room_button.setGeometry(QtCore.QRect(10, 200, 101, 23))
        self.connect_to_room_button.setObjectName("connect_to_room_button")
        self.return_to_rooms_button = QtWidgets.QPushButton(self.room_manager_page)
        self.return_to_rooms_button.setGeometry(QtCore.QRect(10, 20, 101, 23))
        self.return_to_rooms_button.setObjectName("return_to_rooms_button")
        self.current_rooms_box = QtWidgets.QTextBrowser(self.room_manager_page)
        self.current_rooms_box.setGeometry(QtCore.QRect(10, 90, 271, 71))
        self.current_rooms_box.setObjectName("current_rooms_box")
        self.room_browser_box = QtWidgets.QTextBrowser(self.room_manager_page)
        self.room_browser_box.setGeometry(QtCore.QRect(320, 90, 311, 451))
        self.room_browser_box.setObjectName("room_browser_box")
        self.contacts_box = QtWidgets.QTextBrowser(self.room_manager_page)
        self.contacts_box.setGeometry(QtCore.QRect(90, 400, 191, 71))
        self.contacts_box.setObjectName("contacts_box")
        self.current_rooms_scrollbar = QtWidgets.QScrollBar(self.room_manager_page)
        self.current_rooms_scrollbar.setGeometry(QtCore.QRect(290, 90, 16, 71))
        self.current_rooms_scrollbar.setOrientation(QtCore.Qt.Vertical)
        self.current_rooms_scrollbar.setObjectName("current_rooms_scrollbar")
        self.contacts_scrollbar = QtWidgets.QScrollBar(self.room_manager_page)
        self.contacts_scrollbar.setGeometry(QtCore.QRect(290, 400, 16, 71))
        self.contacts_scrollbar.setOrientation(QtCore.Qt.Vertical)
        self.contacts_scrollbar.setObjectName("contacts_scrollbar")
        self.room_browser_scrollbar = QtWidgets.QScrollBar(self.room_manager_page)
        self.room_browser_scrollbar.setGeometry(QtCore.QRect(640, 90, 16, 451))
        self.room_browser_scrollbar.setOrientation(QtCore.Qt.Vertical)
        self.room_browser_scrollbar.setObjectName("room_browser_scrollbar")
        self.stackedWidget.addWidget(self.room_manager_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.connected_rooms.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_lable.setText(_translate("MainWindow", "username"))
        self.password_lable.setText(_translate("MainWindow", "password"))
        self.sign_in_button.setText(_translate("MainWindow", "sign in"))
        self.register_page_button.setText(_translate("MainWindow", "register"))
        self.port_lable.setText(_translate("MainWindow", "port"))
        self.username_lable_reg.setText(_translate("MainWindow", "username"))
        self.password_lable_reg.setText(_translate("MainWindow", "password"))
        self.about_me_lable.setText(_translate("MainWindow", "about me"))
        self.register_button.setText(_translate("MainWindow", "register"))
        self.login_page_button.setText(_translate("MainWindow", "return"))
        self.status_lable.setText(_translate("MainWindow", "status"))
        self.status_state_placeholder.setText(_translate("MainWindow", "status_state"))
        self.send_to_user_button.setText(_translate("MainWindow", "send to user"))
        self.send_all_button.setText(_translate("MainWindow", "send to all"))
        self.send_quit_message.setText(_translate("MainWindow", "quit"))
        self.add_from_contacts_button.setText(_translate("MainWindow", "add to contacts"))
        self.remove_from_contacts_button.setText(_translate("MainWindow", "remove from contacts"))
        self.connected_rooms.setTabText(self.connected_rooms.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.room_manager_button.setText(_translate("MainWindow", "return to room manager"))
        self.ping_contacts_button.setText(_translate("MainWindow", "ping contacts"))
        self.room_browser_lable.setText(_translate("MainWindow", "room browser"))
        self.current_rooms_lable.setText(_translate("MainWindow", "in rooms"))
        self.connect_to_room_button.setText(_translate("MainWindow", "connect to room"))
        self.return_to_rooms_button.setText(_translate("MainWindow", "return to rooms"))
