from PyQt5 import QtWidgets,QtCore,QtGui
from LoginCollab import Ui_MainWindow
from Node_Tools import *
from Node_Builder import *
import sys,hashlib



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
        tmpId = hashlib.sha1(user.encode('utf-8'))
        User_ID = tmpId.hexdigest()
        tmp = ArbolAVL.find(ArbolAVL.root,User_ID)
        if tmp.direccion == User_ID:
            print(tmp.username)
            if tmp.password == password:
                self.ui.label_status.setText("LOGIN REALIZADO")
            else:
                self.ui.label_status.setText("CONTRASEÑA INCORRECTA")
        else:
            self.ui.label_status.setText("ESE USUARIO NO SE ENCUENTRA EN LA BASE")

        
    def RegisterFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]

        """
        logB=LoginBase()
        ref=logB.GetUserDatabase(user)        
        temp=logB.RegisterUser(ref,user,password)
        if temp==False:
            self.ui.label_status.setText("Ya existe ese usuario")
        elif temp==True:
            self.ui.label_status.setText("Se ha registrado el usuario")

        """
if __name__ == '__main__':
    tmp= NodeBuilder()
    AVLDict = tmp.ReadTree()
    AVLTree = tmp.ReconstructTree(AVLDict)
    app= QtWidgets.QApplication([])
    application=MainWindow()
    application.show()
    sys.exit(app.exec())

