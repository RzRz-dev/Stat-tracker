# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_info_user = QtWidgets.QFrame(self.centralwidget)
        self.frame_info_user.setGeometry(QtCore.QRect(1, 1, 491, 331))
        self.frame_info_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info_user.setObjectName("frame_info_user")
        self.frame_png = QtWidgets.QFrame(self.frame_info_user)
        self.frame_png.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.frame_png.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_png.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_png.setObjectName("frame_png")
        self.Label_username = QtWidgets.QLabel(self.frame_info_user)
        self.Label_username.setGeometry(QtCore.QRect(90, 10, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Label_username.setFont(font)
        self.Label_username.setText("")
        self.Label_username.setTextFormat(QtCore.Qt.PlainText)
        self.Label_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_username.setObjectName("Label_username")
        self.ID = QtWidgets.QLabel(self.frame_info_user)
        self.ID.setGeometry(QtCore.QRect(91, 30, 16, 21))
        self.ID.setObjectName("ID")
        self.label_id = QtWidgets.QLabel(self.frame_info_user)
        self.label_id.setGeometry(QtCore.QRect(110, 30, 281, 21))
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.listWidget = QtWidgets.QListWidget(self.frame_info_user)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.frame_info_user)
        self.pushButton.setGeometry(QtCore.QRect(324, 110, 101, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ID.setText(_translate("MainWindow", "ID:"))
        self.pushButton.setText(_translate("MainWindow", "Entrar"))
