from os import access
from PyQt5 import QtWidgets,QtCore,QtGui
from LoginCollab import Ui_MainWindow
from Structures.Node_Tools import *
from Ventana_Info_Juego import Ui_Juego
from ImageManager import ImageManager
from User_menu import Ui_UserMenu
from DataBase import LoginBase
from CelesteData import Access_to_a_file
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
import sys,json,requests
import matplotlib.pyplot as plot

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.resize(900, 700)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Login_Button.clicked.connect(self.LoginFunc)
        self.ui.Register_Button.clicked.connect(self.RegisterFunc)
        self.cont=0
        self.dic={}


    def InputReceive(self):
        self.user=self.ui.Input_User.text()
        self.password=self.ui.Input_Password.text()
        return self.user,self.password
    
    def LoginFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password=datos[1]
        tmpId = mapa_user.HashFunc(user)
        self.User_ID = hex(tmpId)
        if mapa_user.HasKey(user) == False:
            msj= "Ese usuario no está registrado"
            self.ui.label_status.setText(msj)
        elif mapa_user.HasKey(user) == True:
            tmpN=mapa_user.Get(user)
            if tmpN["password"] == password:
                msj= "LOGIN EXITOSO"
                self.user=user
                self.MostrarMenuUser()
            else:
                msj= "CONTRASEÑA INCORRECTA"
                self.ui.label_status.setText(msj)
        

    def RegisterFunc(self):
        datos = self.InputReceive()
        user=datos[0]
        password_=datos[1]
        tmpId = mapa_user.HashFunc(user)
        UserID_ = hex(tmpId)
        if mapa_user.HasKey(user) == True:
            msj ="Ese usuario no está disponible"
        elif mapa_user.HasKey(user) == False:
            tmp=dict(UserID=UserID_,password=password_)
            mapa_user.Set(user,tmp)
            msj= "Registrado"
            builder.SaveData("scr\Datos\Data_Users.json",mapa_user)

        self.ui.label_status.setText(msj)


    def MostrarMenuUser(self):
        self.ui=Ui_UserMenu()
        self.ui.setupUi(self)
        self.ui.Label_username.setText(self.user)
        self.ui.label_id.setText(self.User_ID)
        self.SetLogButton()

        tmp=ImageManager()
        url_image_user = tmp.GetUrl_Image("usuarios","aaa")
        image_user = QtGui.QImage()
        image_user.loadFromData(requests.get(url_image_user).content)
        self.ui.label_png.setPixmap(QtGui.QPixmap(image_user))
        temp= LoginBase()        
        games=temp.GetGamesNames()
        for i in games:
            self.ui.listWidget.addItem(i)
        self.ui.pushButton.clicked.connect(self.GetGame)
        self.ui.Unlog_button.clicked.connect(self.Log)
        

    def Log(self):
        self.resize(900, 700)
        self.user = None
        self.User_ID = None
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Login_Button.clicked.connect(self.LoginFunc)
        self.ui.Register_Button.clicked.connect(self.RegisterFunc)

    def Back(self):
        self.resize(900, 700)
        self.ui=Ui_UserMenu()
        self.ui.setupUi(self)
        self.SetLogButton()

        tmp=ImageManager()
        url_image_user = tmp.GetUrl_Image("usuarios","aaa")
        image_user = QtGui.QImage()
        image_user.loadFromData(requests.get(url_image_user).content)
        self.ui.label_png.setPixmap(QtGui.QPixmap(image_user))
        temp= LoginBase()        
        games=temp.GetGamesNames()
        for i in games:
            self.ui.listWidget.addItem(i)
        self.ui.pushButton.clicked.connect(self.GetGame)
        self.ui.Unlog_button.clicked.connect(self.Log)
        
        

    def GetGame(self):
        try:
            actual=self.ui.listWidget.currentItem().text()
            self.MostrarInfoJuego(actual)
        except AttributeError:
            None

    def MostrarInfoJuego(self,juego):
        def CallThisWindow():
            self.MostrarInfoJuego(juego)
        
        def CreateGraph():

            CallThisWindow()
            x=self.ui.widget_Graph.layout()
            tmp=juego+"_"+self.user
            data=mapa_games.Get(tmp)
            opc =[]
            if data.get("Estatico")!=None:
                tempdic1=data["Estatico"]
            else:
                tempdic1={}

            if data.get("Infinito")!=None:
                tempdic2=data["Infinito"]
            else:
                tempdic2={}
                
            for i in tempdic1:
                opc.append(i)
            for i in tempdic2:
                opc.append(i)
            stat,xx = QtWidgets.QInputDialog.getItem(
            self, 'Menú de stats', 'Seleccione el stat que desea ver:', opc,0,False)

            if xx == False:
                return
            
            if tempdic1.get(stat)!=None:
                x=int(tempdic1.get(stat))
                limite = LoginBase()
                y=limite.GetGameLimits(juego)
                total = y.get(stat)
                faltantes = total - x
                series  = QPieSeries()
                series.append(str("Obtenido") ,x)
                series.append(str("Faltante"),faltantes)
                series.setLabelsVisible()
                series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)

                slice1=series.slices()[0]
                slice2=series.slices()[1]
                porc1=100 * slice1.percentage()
                porc1=round(porc1, 2)
                porc2=100 * slice2.percentage()
                porc2=round(porc2, 2)
                slice1.setLabel("Obtenido: "+str(porc1)+"%")
                slice2.setLabel("Faltante: "+str(porc2)+"%")

                Resaltado = series.slices()[0]
                Resaltado.setExploded(True)
                Resaltado.setLabelVisible(True)
                Resaltado.setPen(QtGui.QPen(QtCore.Qt.green, 4))
                Resaltado.setBrush(QtCore.Qt.green)

                chart = QChart()
                chart.addSeries(series)
                chart.setAnimationOptions(QChart.SeriesAnimations)
                chart.setTitle("Stat View: " + str(stat))
            
            if tempdic2.get(stat)!=None:
                x=tempdic2.get(stat)
                set0 = QBarSet(stat)
                for i in x:
                    set0.append(i)
                print(x)
                series = QBarSeries()
                series.append(set0)
                chart = QChart()
                chart.addSeries(series)
                chart.setAnimationOptions(QChart.SeriesAnimations)
                chart.setTitle("Stat View: " + str(stat))

                axisX = QBarCategoryAxis()
                xs=[]
                for e in range(0,len(x)):
                    xs.append(str(e))
                axisX.append(xs)
                chart.addAxis(axisX, QtCore.Qt.AlignBottom)
                series.attachAxis(axisX)

                axisY = QValueAxis()
                axisY.setRange(0,max(x))
                chart.addAxis(axisY, QtCore.Qt.AlignLeft)
                series.attachAxis(axisY)
                chart.legend().setVisible(True)
                chart.legend().setAlignment(QtCore.Qt.AlignBottom)


            chart.setTheme(QChart.ChartThemeDark)
            chartview = QChartView(chart)
            vbox = QtWidgets.QVBoxLayout()
            vbox.addWidget(chartview)
            self.ui.widget_Graph.setLayout(vbox)

            '''
            chart = QChart()
            chart.addSeries(series)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart.setTitle("Stat View")
            chart.setTheme(QChart.ChartThemeDark)
            chartview = QChartView(chart)
            vbox = QtWidgets.QVBoxLayout()
            vbox.addWidget(chartview)
            self.ui.widget_Graph.setLayout(vbox)
            '''

        def UpdateStats():
            tmp=juego+"_"+self.user
            data=mapa_games.Get(tmp)
            opc =[]
            tempdic1=data["Estatico"]
            tempdic2=data["Infinito"]
            for i in tempdic1:
                opc.append(i)
            for i in tempdic2:
                opc.append(i)
            stat,xx = QtWidgets.QInputDialog.getItem(
            self, 'Menú de stats', 'Seleccione el stat que desea editar:', opc,0,False)

            if xx == False:
                return

            value,yy = QtWidgets.QInputDialog.getInt(
            self, 'Establecer valor', 'Digite el nuevo valor del stat:')  
            
            if yy == False:
                return

            if xx and yy:
                if tempdic1.get(stat)!=None:
                    dic={stat:value}
                    tempdic1.update(dic)
                    data["Estatico"]=tempdic1
                    mapa_games.Set(tmp,data)
                    builder.SaveData("scr\Datos\Data_Games.json",mapa_games)
                    CallThisWindow()
                elif tempdic2.get(stat)!=None:
                    datos=tempdic2.get(stat)
                    datos.append(value)
                    if len(datos) > 7:
                        datos.pop(0)
                    tempdic2[stat]=datos
                    data["Infinito"]=tempdic2
                    mapa_games.Set(tmp,data)
                    builder.SaveData("scr\Datos\Data_Games.json",mapa_games)
                    CallThisWindow()

        def UpdateFromDoc():
            if juego == "Celeste":
                temp= Access_to_a_file('celeste', '0.celeste', 'celestepath.txt')
                info = temp.get_celeste_data(temp.get_path_to_file())
                if info != None:
                    tmp=juego+"_"+self.user
                    data=mapa_games.Get(tmp)
                    tempdic1=data["Estatico"]
                    keys1=tempdic1.keys()
                    tempdic2=data["Infinito"]
                    keys2=tempdic2.keys()
                    con = 0
                    for i in keys1:
                        tempdic1.update({i:info[con]})
                        con=con+1
                    for i in keys2:
                        infout = tempdic2[i]
                        infout.append(info[con])
                        tempdic2.update({i:infout})
                        con=con+1
                    data["Estatico"]=tempdic1
                    data["Infinito"]=tempdic2
                    mapa_games.Set(tmp,data)
                    builder.SaveData("scr\Datos\Data_Games.json",mapa_games)

                    
                
            elif juego == "Risk of Rain 2":
                temp1 = Access_to_a_file('riskofrain2', 'PreviousRun.xml', 'riskofrain2patha.txt')
                fileNameRoR2 = temp1.get_ror2_data_file(temp1.get_path_to_file())
                temp2 = Access_to_a_file('riskofrain2', fileNameRoR2, 'riskofrain2pathb.txt')
                info2 = temp2.get_ror2_data(temp2.get_path_to_file())
                if info2 != None:
                    tmp=juego+"_"+self.user
                    data=mapa_games.Get(tmp)
                    tempdic1=data["Infinito"]
                    keys1=tempdic1.keys()
                    con = 0
                    for i in keys1:
                        infout = tempdic1[i]
                        infout.append(info2[con])
                        tempdic1.update({i:infout})
                        con=con+1
                    data["Infinito"]=tempdic1
                    mapa_games.Set(tmp,data)
                    builder.SaveData("scr\Datos\Data_Games.json",mapa_games)
            
            CallThisWindow()

        self.ui=Ui_Juego()
        self.ui.setupUi(self)
        self.juego_ref = juego
        self.ui.label_nombre.setText(self.user)
        self.ui.label_juego.setText(juego)
        self.RellenarTabla(juego)
        self.SetBackButton()
        self.SetImages(juego)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.pushButton_Edit.clicked.connect(UpdateStats)
        self.ui.pushButton_View.clicked.connect(CreateGraph)
        self.ui.pushButton_Edit_2.clicked.connect(UpdateFromDoc)
        self.ui.Unlog_button.clicked.connect(self.Log)
        self.ui.Return_button.clicked.connect(self.Back)
        
    

    def SetLogButton(self):
        temp=ImageManager()
        url_image_unlog = temp.GetUrl_Image("varios","unlog_icon.png")
        image_unlog = QtGui.QImage()
        image_unlog.loadFromData(requests.get(url_image_unlog).content)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image_unlog), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.Unlog_button.setIcon(icon)

    def SetBackButton(self):
        temp=ImageManager()
        url_image_unlog = temp.GetUrl_Image("varios","back_icon.png")
        image_unlog = QtGui.QImage()
        image_unlog.loadFromData(requests.get(url_image_unlog).content)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image_unlog), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.Return_button.setIcon(icon)

    def SetImages(self,x):
        temp=ImageManager()
        url_image_game = temp.GetUrl_Image("juegos",x)
        url_image_user = temp.GetUrl_Image("usuarios","aaa")
        image_game = QtGui.QImage()
        image_game.loadFromData(requests.get(url_image_game).content)
        image_user = QtGui.QImage()
        image_user.loadFromData(requests.get(url_image_user).content)
        self.ui.png_game.setPixmap(QtGui.QPixmap(image_game))
        self.ui.png_user.setPixmap(QtGui.QPixmap(image_user))
        self.SetLogButton()


    def RellenarTabla(self,juego):
        tmp=juego+"_"+self.user
        if mapa_games.HasKey(tmp) == False:
            temp=LoginBase()
            lista=temp.GetPlayerInfo("Dummy",juego)
            cont=0
            
            if lista.get("Estatico")!= None:
                tempdic1=lista["Estatico"]
                for i in tempdic1:
                    self.ui.tableWidget.insertRow(cont)
                    celda1 = QtWidgets.QTableWidgetItem(i)
                    celda2 = QtWidgets.QTableWidgetItem(str(tempdic1.get(i)))
                    self.ui.tableWidget.setItem(cont,0,celda1)
                    self.ui.tableWidget.setItem(cont,1,celda2)    
                    cont +=1
            
            if lista.get("Infinito")!= None:
                tempdic2=lista["Infinito"]
            
                for i in tempdic2:
                    self.ui.tableWidget.insertRow(cont)
                    celda1 = QtWidgets.QTableWidgetItem(i)
                    celda2 = QtWidgets.QTableWidgetItem(str(tempdic2.get(i)))
                    self.ui.tableWidget.setItem(cont,0,celda1)
                    self.ui.tableWidget.setItem(cont,1,celda2)    
                    cont +=1

                relleno={}
                for i in tempdic2:
                    x = {i:[0]}
                    relleno.update(x)
                y = {"Infinito":relleno}
                lista.update(y)
            mapa_games.Set(tmp,lista)
            builder.SaveData("scr\Datos\Data_Games.json",mapa_games)   
        else:
            data=mapa_games.Get(tmp)
            cont=0
            if data.get("Estatico")!= None:
                tempdic1=data["Estatico"]
                for i in tempdic1:
                    self.ui.tableWidget.insertRow(cont)
                    celda1 = QtWidgets.QTableWidgetItem(i)
                    celda2 = QtWidgets.QTableWidgetItem(str(tempdic1.get(i)))
                    self.ui.tableWidget.setItem(cont,0,celda1)
                    self.ui.tableWidget.setItem(cont,1,celda2)    
                    cont +=1
            if data.get("Infinito")!= None:
                tempdic2=data["Infinito"]
        
                for i in tempdic2:
                    self.ui.tableWidget.insertRow(cont)
                    celda1 = QtWidgets.QTableWidgetItem(i)
                    num=tempdic2.get(i)
                    celda2 = QtWidgets.QTableWidgetItem(str(num[-1]))
                    self.ui.tableWidget.setItem(cont,0,celda1)
                    self.ui.tableWidget.setItem(cont,1,celda2)    
                    cont +=1
            self.ui.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    builder = HashBuilder()
    mapa_user= Nmap()
    builder.ReadData("scr\Datos\Data_Users.json",mapa_user)
    mapa_games=Nmap()
    builder.ReadData("scr\Datos\Data_Games.json",mapa_games)
    
    app= QtWidgets.QApplication([])
    application=MainWindow()
    application.show()
    sys.exit(app.exec())
