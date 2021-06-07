from PyQt5 import QtWidgets
from LoginCollab import Ui_MainWindow
import sys
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Login_Button.clicked.connect(self.LoginFunc)
        self.ui.Register_Button.clicked.connect(self.RegisterFunc)
        self.cont=0
    
    def InputReceive(self):
        user=self.ui.Input_User.text()
        password=self.ui.Input_Password.text()
        return user,password
    
    def LoginFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]
        baseDatos=open(".scr\cuentas.txt","r")
        while True:
            tempString=baseDatos.readline()
            tempInfo= tempString.split("#")
            print(tempInfo)
            user_B=tempInfo[0]
            if user_B=="":
                self.ui.label_status.setText("User not found")
                break
            contra_B=tempInfo[1]
            if user_B==user:
                if contra_B==password:
                    self.ui.label_status.setText("Logged")
                    break
                else:
                    self.ui.label_status.setText("Wrong password")
                    break
        baseDatos.close()

        
    def RegisterFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]
        print
        cuentas = open("cuentas.txt", "r")
        while True:
            tempString=cuentas.readline()
            if tempString=="":
                cuentas.close()
                cuentas = open('cuentas.txt', "a")
                cuentas.write(user+"#"+password+"#\n")
                self.ui.label_status.setText("Registered")
                break
            else:
                tempUser= tempString.split("#")
                if tempUser[0] == user:
                    self.ui.label_status.setText("User already exists")
                    break
        cuentas.close()
    

app= QtWidgets.QApplication([])
application=Login()
application.show()
sys.exit(app.exec())
