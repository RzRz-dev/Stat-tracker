from PyQt5 import QtWidgets,QtCore,QtGui
from LoginCollab import Ui_MainWindow
from DataBase import LoginBase
from User_menu import Ui_UserMenu
from Ventana_Info_Juego import Ui_Juego
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
        self.ui=Ui_Juego()
        self.ui.setupUi(self)
        temp=LoginBase()
        lista=temp.GetPlayerInfo(self.id,juego)
        llaves=lista.keys()
        valores=lista.values()
        for i in llaves:
            self.ui.listWidget.addItem(i)
        for i in valores:
            self.ui.listWidget_2.addItem(str(i))
        #Arreglar el Ventana_Info_Juego para que sea una tabla con 2 columnas
        #Revisar si es posible empotrar ventanas en un frame
        #Agregar imágenes si es posible en los frames
            

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

