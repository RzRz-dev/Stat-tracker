from PyQt5 import QtWidgets,QtCore,QtGui
from LoginCollab import Ui_MainWindow
from DataBase import LoginBase
from User_menu import Ui_UserMenu
import requests
from Ventana_Info_Juego import Ui_Juego
from ImageManager import ImageManager
import sys
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.resize(900, 700)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Login_Button.clicked.connect(self.LoginFunc)
        self.ui.Register_Button.clicked.connect(self.RegisterFunc)
        self.cont=0
        

    def InputReceive(self):
        self.user=self.ui.Input_User.text()
        self.password=self.ui.Input_Password.text()
        return self.user,self.password
    
    def LoginFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]
        
        logB=LoginBase()
        ref=logB.GetUserDatabase(user)
        temp=logB.LoginUser(ref,password)
        self.ui.label_status.setText(temp)
        if temp=="Entrando":
            self.MostrarMenuUser()
    
    def MostrarMenuUser(self):
        self.ui=Ui_UserMenu()
        self.ui.setupUi(self)
        self.ui.Label_username.setText(self.user)
        temp= LoginBase()
        self.id=temp.GetId(self.user)
        self.ui.label_id.setText(self.id)
        games=temp.GetGamesNames()
        for i in games:
            self.ui.listWidget.addItem(i)
        self.ui.pushButton.clicked.connect(self.GetGame)

    def GetGame(self):
        try:
            actual=self.ui.listWidget.currentItem().text()
            self.MostrarInfoJuego(actual)
        except AttributeError:
            None
    
    def MostrarInfoJuego(self,juego):
        def CallThisWindow():
            self.MostrarInfoJuego(juego)
        
        self.ui=Ui_Juego()
        self.ui.setupUi(self)
        self.juego_ref = juego
        self.ui.label_nombre.setText(self.user)
        self.ui.label_juego.setText(juego)
        self.RellenarTabla(juego)
        self.SetImages(juego)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.pushButton_Edit.clicked.connect(CallThisWindow)
        
        #Hacer los popups de los botones
        #Agregar las funciones de los botones

    def SetImages(self,x):
        temp=ImageManager()
        url_image_game = temp.GetUrl_Image("juegos",x)
        url_image_user = temp.GetUrl_Image("usuarios",self.user)
        image_game = QtGui.QImage()
        image_game.loadFromData(requests.get(url_image_game).content)
        image_user = QtGui.QImage()
        image_user.loadFromData(requests.get(url_image_user).content)
        self.ui.png_game.setPixmap(QtGui.QPixmap(image_game))
        self.ui.png_user.setPixmap(QtGui.QPixmap(image_user))

    def RellenarTabla(self,juego):
        temp=LoginBase()
        lista=temp.GetPlayerInfo(self.id,juego)
        cont=0
        for i in lista:
            self.ui.tableWidget.insertRow(cont)
            celda1 = QtWidgets.QTableWidgetItem(i)
            celda2 = QtWidgets.QTableWidgetItem(str(lista.get(i)))
            self.ui.tableWidget.setItem(cont,0,celda1)
            self.ui.tableWidget.setItem(cont,1,celda2)
            cont +=1


    def RegisterFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]
        logB=LoginBase()
        ref=logB.GetUserDatabase(user)        
        temp=logB.RegisterUser(ref,user,password)
        if temp==False:
            self.ui.label_status.setText("Ya existe ese usuario")
        elif temp==True:
            self.ui.label_status.setText("Se ha registrado el usuario")

app= QtWidgets.QApplication([])
application=MainWindow()
application.show()
sys.exit(app.exec())

