from PyQt5 import QtWidgets,QtCore,QtGui
from LoginCollab import Ui_MainWindow
from DataBase import LoginBase
from User_menu import Ui_UserMenu
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


    #arreglar   
    """
        self.ui.pushButton.clicked.connect(self.GetGame)
    def GetGame(self):
        actual=self.ui.listWidget.currentRow()
        game=actual.getText()
        print(game)

        #hacer funcion que obtenga id y ruta del juego
    """

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

