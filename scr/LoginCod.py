from PyQt5 import QtWidgets
from LoginCollab import Ui_MainWindow
from DataBase import LoginBase
import sys
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Login_Button.clicked.connect(self.LoginFunc)
        self.ui.Register_Button.clicked.connect(self.RegisterFunc)
        self.cont=0
        self.id=5
    
    def InputReceive(self):
        user=self.ui.Input_User.text()
        password=self.ui.Input_Password.text()
        return user,password
    
    def LoginFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]
        
        logB=LoginBase()
        ref=logB.GetUserDatabase(user)
        logB.LoginUser(ref,password)
        
    def RegisterFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]
        logB=LoginBase()
        ref=logB.GetUserDatabase(user)        
        logB.RegisterUser(ref,user,password,self.id)
        self.id+=1

app= QtWidgets.QApplication([])
application=Login()
application.show()
sys.exit(app.exec())
