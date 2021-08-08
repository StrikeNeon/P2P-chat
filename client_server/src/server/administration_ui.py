# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administration_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class room_tab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.close_room_button = QtWidgets.QPushButton(self)
        self.close_room_button.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.close_room_button.setObjectName("close_room_button")
        self.room_num_lable = QtWidgets.QLabel(self)
        self.room_num_lable.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.room_num_lable.setObjectName("room_num_lable")
        self.user_counter_lable = QtWidgets.QLabel(self)
        self.user_counter_lable.setGeometry(QtCore.QRect(120, 20, 61, 16))
        self.user_counter_lable.setObjectName("user_counter_lable")
        self.user_counter = QtWidgets.QLCDNumber(self)
        self.user_counter.setGeometry(QtCore.QRect(120, 50, 64, 23))
        self.user_counter.setObjectName("user_counter")
        self.room_num_placeholder = QtWidgets.QLabel(self)
        self.room_num_placeholder.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.room_num_placeholder.setObjectName("room_num_placeholder")
        self.room_load_display = QtWidgets.QProgressBar(self)
        self.room_load_display.setGeometry(QtCore.QRect(20, 120, 118, 23))
        self.room_load_display.setProperty("value", 0)
        self.room_load_display.setObjectName("room_load_display")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.label.setObjectName("label")
        self.log_box = QtWidgets.QTextBrowser(self)
        self.log_box.setGeometry(QtCore.QRect(220, 10, 511, 321))
        self.log_box.setObjectName("log_box")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 771, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.room_management_page = QtWidgets.QWidget()
        self.room_management_page.setObjectName("room_management_page")
        self.room_manager = QtWidgets.QTabWidget(self.room_management_page)
        self.room_manager.setGeometry(QtCore.QRect(20, 20, 751, 391))
        self.room_manager.setObjectName("room_manager")
        self.room_zero_tab = room_tab()

        self.room_manager.addTab(self.room_zero_tab, "room_zero_tab")
        self.db_reconnect_button = QtWidgets.QPushButton(self.room_management_page)
        self.db_reconnect_button.setGeometry(QtCore.QRect(20, 450, 101, 23))
        self.db_reconnect_button.setObjectName("db_reconnect_button")
        self.enable_debug_log = QtWidgets.QCheckBox(self.room_management_page)
        self.enable_debug_log.setGeometry(QtCore.QRect(20, 480, 70, 17))
        self.enable_debug_log.setObjectName("enable_debug_log")
        self.db_log_box = QtWidgets.QTextBrowser(self.room_management_page)
        self.db_log_box.setGeometry(QtCore.QRect(150, 450, 601, 131))
        self.db_log_box.setObjectName("db_log_box")
        self.stackedWidget.addWidget(self.room_management_page)
        self.log_in_page = QtWidgets.QWidget()
        self.log_in_page.setObjectName("log_in_page")
        self.start_server = QtWidgets.QPushButton(self.log_in_page)
        self.start_server.setGeometry(QtCore.QRect(270, 220, 75, 23))
        self.start_server.setObjectName("start_server")
        self.login_lable = QtWidgets.QLabel(self.log_in_page)
        self.login_lable.setGeometry(QtCore.QRect(270, 150, 47, 13))
        self.login_lable.setObjectName("login_lable")
        self.password_lable = QtWidgets.QLabel(self.log_in_page)
        self.password_lable.setGeometry(QtCore.QRect(270, 180, 47, 13))
        self.password_lable.setObjectName("password_lable")
        self.login_input = QtWidgets.QLineEdit(self.log_in_page)
        self.login_input.setGeometry(QtCore.QRect(330, 150, 113, 20))
        self.login_input.setObjectName("login_input")
        self.password_input = QtWidgets.QLineEdit(self.log_in_page)
        self.password_input.setGeometry(QtCore.QRect(330, 180, 113, 20))
        self.password_input.setObjectName("password_input")
        self.stackedWidget.addWidget(self.log_in_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.room_manager.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.room_zero_tab.close_room_button.setText(_translate("MainWindow", "close room"))
        self.room_zero_tab.room_num_lable.setText(_translate("MainWindow", "room_num"))
        self.room_zero_tab.user_counter_lable.setText(_translate("MainWindow", "users online"))
        self.room_zero_tab.room_num_placeholder.setText(_translate("MainWindow", "placeholder_num"))
        self.room_zero_tab.label.setText(_translate("MainWindow", "room load"))
        self.room_manager.setTabText(self.room_manager.indexOf(self.room_zero_tab), _translate("MainWindow", "Tab 1"))
        self.db_reconnect_button.setText(_translate("MainWindow", "reconnect mongo"))
        self.enable_debug_log.setText(_translate("MainWindow", "debug logs"))
        self.start_server.setText(_translate("MainWindow", "administrate"))
        self.login_lable.setText(_translate("MainWindow", "login"))
        self.password_lable.setText(_translate("MainWindow", "password"))
