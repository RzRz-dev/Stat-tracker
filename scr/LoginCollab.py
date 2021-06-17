# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginCollab.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(325, 230, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(325, 280, 100, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(410, 340, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.Login_Button.setFont(font)
        self.Login_Button.setObjectName("Login_Button")
        self.Register_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Register_Button.setGeometry(QtCore.QRect(410, 376, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.Register_Button.setFont(font)
        self.Register_Button.setObjectName("Register_Button")
        self.Input_User = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_User.setGeometry(QtCore.QRect(325, 250, 250, 21))
        self.Input_User.setText("")
        self.Input_User.setMaxLength(30)
        self.Input_User.setObjectName("Input_User")
        self.Input_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_Password.setGeometry(QtCore.QRect(325, 300, 250, 21))
        self.Input_Password.setText("")
        self.Input_Password.setMaxLength(30)
        self.Input_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Input_Password.setObjectName("Input_Password")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(325, 420, 250, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_user.setText(_translate("MainWindow", "User"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.Login_Button.setText(_translate("MainWindow", "Login"))
        self.Register_Button.setText(_translate("MainWindow", "Register"))
        self.Input_User.setPlaceholderText(_translate("MainWindow", "Username"))
        self.Input_Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_status.setText(_translate("MainWindow", ""))
