# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_Info_Juego.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Juego(object):
    def setupUi(self, Juego):
        Juego.setObjectName("Juego")
        Juego.resize(623, 708)
        Juego.setStyleSheet("QWidget\n"
"{\n"
"    background-color: #1a1a1a;\n"
"    color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #c2c7d5;\n"
"    font-size: 13px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #fff;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #ff4747;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #ff3333;\n"
"    border: 1px solid #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #c2c7d5;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"    background-color: #333333;\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #191919;\n"
"    show-decoration-selected: 0;\n"
"    padding-left: -13px;\n"
"    padding-right: -13px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"    color: #31cecb;\n"
"    background-color: #454e5e;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    padding-left : 10px;\n"
"    height: 42px;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"    color: #000;\n"
"    background-color: #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"    color:white;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"    color: #000;\n"
"    background-color: #bcbdbb;\n"
"    border: none;\n"
"    padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"    background-color: #252525;\n"
"    show-decoration-selected: 0;\n"
"    color: #c2c8d7;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #252525;\n"
"    border: 1px solid gray;\n"
"    color: #f0f0f0;\n"
"    gridline-color: gray;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #ff3333;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #343a49;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    color: #fff;\n"
"    border-top: 0px;\n"
"    border-bottom: 1px solid gray;\n"
"    border-right: 1px solid gray;\n"
"    background-color: #343a49;\n"
"    margin-top:1px;\n"
"    margin-bottom:1px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #000;\n"
"    background-color: #ff3333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #9b9b9b;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #9b9b9b;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Juego)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Edit.setGeometry(QtCore.QRect(410, 260, 70, 23))
        self.pushButton_Edit.setObjectName("pushButton_Edit")
        self.pushButton_View = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_View.setGeometry(QtCore.QRect(410, 300, 70, 23))
        self.pushButton_View.setObjectName("pushButton_View")
        self.label_nombre = QtWidgets.QLabel(self.centralwidget)
        self.label_nombre.setGeometry(QtCore.QRect(140, 10, 411, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombre.setFont(font)
        self.label_nombre.setText("")
        self.label_nombre.setObjectName("label_nombre")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 260, 210, 341))
        self.tableWidget.setMinimumSize(QtCore.QSize(210, 341))
        self.tableWidget.setMaximumSize(QtCore.QSize(210, 341))
        self.tableWidget.setToolTipDuration(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 120, 120))
        self.frame.setToolTipDuration(0)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.png_user = QtWidgets.QLabel(self.frame)
        self.png_user.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.png_user.setText("")
        self.png_user.setScaledContents(True)
        self.png_user.setObjectName("png_user")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 170, 441, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_juego = QtWidgets.QLabel(self.frame_2)
        self.label_juego.setGeometry(QtCore.QRect(90, 10, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_juego.setFont(font)
        self.label_juego.setToolTipDuration(0)
        self.label_juego.setText("")
        self.label_juego.setObjectName("label_juego")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.png_game = QtWidgets.QLabel(self.frame_3)
        self.png_game.setGeometry(QtCore.QRect(1, 1, 78, 78))
        self.png_game.setFrameShape(QtWidgets.QFrame.Box)
        self.png_game.setText("")
        self.png_game.setPixmap(QtGui.QPixmap("cuenta.png"))
        self.png_game.setScaledContents(True)
        self.png_game.setAlignment(QtCore.Qt.AlignCenter)
        self.png_game.setObjectName("png_game")
        self.Unlog_button = QtWidgets.QPushButton(self.centralwidget)
        self.Unlog_button.setGeometry(QtCore.QRect(560, 10, 45, 45))
        self.Unlog_button.setToolTipDuration(0)
        self.Unlog_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/unlog_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Unlog_button.setIcon(icon)
        self.Unlog_button.setIconSize(QtCore.QSize(35, 35))
        self.Unlog_button.setFlat(False)
        self.Unlog_button.setObjectName("Unlog_button")
        self.widget_Graph = QtWidgets.QWidget(self.centralwidget)
        self.widget_Graph.setGeometry(QtCore.QRect(300, 334, 291, 261))
        self.widget_Graph.setObjectName("widget_Graph")
        self.pushButton_Edit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Edit_2.setGeometry(QtCore.QRect(289, 280, 101, 20))
        self.pushButton_Edit_2.setObjectName("pushButton_Edit_2")
        self.Return_button = QtWidgets.QPushButton(self.centralwidget)
        self.Return_button.setGeometry(QtCore.QRect(560, 60, 45, 45))
        self.Return_button.setToolTipDuration(0)
        self.Return_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Return_button.setIcon(icon1)
        self.Return_button.setIconSize(QtCore.QSize(35, 35))
        self.Return_button.setFlat(False)
        self.Return_button.setObjectName("Return_button")
        Juego.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Juego)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName("menubar")
        Juego.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Juego)
        self.statusbar.setObjectName("statusbar")
        Juego.setStatusBar(self.statusbar)

        self.retranslateUi(Juego)
        QtCore.QMetaObject.connectSlotsByName(Juego)

    def retranslateUi(self, Juego):
        _translate = QtCore.QCoreApplication.translate
        Juego.setWindowTitle(_translate("Juego", "MainWindow"))
        self.pushButton_Edit.setText(_translate("Juego", "Editar"))
        self.pushButton_View.setText(_translate("Juego", "Ver"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Juego", "Stats"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Juego", "Value"))
        self.pushButton_Edit_2.setText(_translate("Juego", "Obtener Datos"))
