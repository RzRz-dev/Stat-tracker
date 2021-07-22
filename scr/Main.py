import hashlib
from LOL_Info import LOL_Info
from Node_Builder import *
from Node_Tools import *
import time
import profile


class CmdUI:
    def __init__(self):
        self.tmp_U = NodeBuilder("scr\Datos\ArbolUsers.json")
        self.AVLDict_U = self.tmp_U.ReadTree()
        self.AVLTree_U = self.tmp_U.ReconstructTree(self.AVLDict_U)
        self.tmp_D = NodeBuilder("scr\Datos\ArbolData.json")
        self.AVLDict_D = self.tmp_D.ReadTree()
        self.AVLTree_D = self.tmp_D.ReconstructTree(self.AVLDict_D)
        self.usercode=None
        self.LoginView()
        input("Presione cualquier tecla para continuar")

    def LoginView(self):
        while True:
            print("\n"+"Que desea hacer:"+"\n"+"1.Login"+"\n"+"2.Register"+"\n"+"3.Exit"+"\n")
            op = str(input())
            if op =="1":
                user=str(input("Ingrese su usuario:  "))
                password=str(input("Ingrese su contraseña:  "))
                tmpId = hashlib.sha1(user.encode('utf-8'))
                User_ID = tmpId.hexdigest()
                Node_ID = "User_" + str(User_ID)
                
                tmp = self.AVLTree_U.find(self.AVLTree_U.root,Node_ID)
                if tmp == None:
                    print("ESE USUARIO NO SE ENCUENTRA EN LA BASE")
                elif tmp.direccion == Node_ID:
                    print(tmp.username)
                    if tmp.password == password:
                        print("LOGIN REALIZADO"+"\n")
                        self.usercode = User_ID
                        self.GameView()
                    else:
                        print("CONTRASEÑA INCORRECTA")
                else:
                    print("ESE USUARIO NO SE ENCUENTRA EN LA BASE")

            elif op =="2":
                user=str(input("Ingrese su usuario:  "))
                password=str(input("Ingrese su contraseña:  "))
                tmpId = hashlib.sha1(user.encode('utf-8'))
                User_ID = tmpId.hexdigest()
                Node_ID = "User_" + str(User_ID)
                tmp = self.AVLTree_U.find(self.AVLTree_U.root,Node_ID)
                if tmp == None:
                    print("SE REGISTRARÁ EL USUARIO")
                    nodo = Node_User(Node_ID,user,password)
                    self.AVLTree_U.AVLinsert(nodo)
                    self.AVLTree_U.InOrderTrav(self.AVLTree_U.root)
                elif tmp.direccion == Node_ID:
                    print("ESE USUARIO YA ESTÁ REGISTRADO")
                else:
                    print("SE REGISTRARÁ EL USUARIO")
                    nodo = Node_User(Node_ID,user,password)
                    self.AVLTree_U.AVLinsert(nodo)
                    self.AVLTree_U.InOrderTrav(self.AVLTree_U.root)
            elif op == "3":
                self.AVLDict_U = self.tmp_U.InOrderTrav_Dict(self.AVLTree_U.root,self.AVLDict_U)
                self.tmp_U.SaveTree(self.AVLDict_U)
                print("PROGRAMA TERMINADO")
                break
            else:
                self.AVLDict_U = self.tmp_U.InOrderTrav_Dict(self.AVLTree_U.root,self.AVLDict_U)
                self.tmp_U.SaveTree(self.AVLDict_U)
                print("PROGRAMA TERMINADO")
                break

    def GameView(self):
        while self.usercode != None:
            menu1=input("Enter a game to start"+'\n'+"Available: LOL, Celeste, Jump King (JK), Risk of Rain 2 (RoR2)"+'\n'+"\n")
            menu1 = menu1.lower()
            
            if menu1=="lol":
                print("\n"+"userbase not implemented"+"\n")
                LOL = LOL_Info()
                while True:
                    LOL.start_Stats()
                    LOL.get_info()
                    menu2=input("¿Do you want to get stats from another account?"+'\n'+"enter y(yes) or n(no) to continue"'\n')
                    if menu2=="n":
                        break
            elif menu1 == "celeste":
                while True:
                    choise = input("\n"+"Que desea hacer:"+"\n"+"1.Ver datos de juego"+"\n"+"2.Actualizar datos"+"\n"+"Ingrese cualquier cosa para volver"+"\n"+"\n")
                    if choise == "1":
                        datadir="Celeste_"+ self.usercode
                        data = self.AVLTree_D.find(self.AVLTree_D.root,datadir)
                        if data == None:
                            print("Datos no existentes"+"\n")
                        elif data.direccion != datadir:
                            print ("Datos no existentes"+"\n")
                        else:
                            self.PrintInfo(data)
                        
                    elif choise == "2":
                        datadir="Celeste_"+ self.usercode
                        fresas = str(input("fresas =  "))
                        caras= str(input("caras =  "))
                        tiempo= str(input("tiempo =  "))
                        muertes= str(input("muertes =  "))
                        niveles= str(input("niveles =  "))
                        data = self.AVLTree_D.find(self.AVLTree_D.root,datadir)
                        if data == None:
                            print("Datos no existentes, creando nuevo"+"\n")
                            nodo = Node_Celeste(datadir,fresas,caras,tiempo,muertes,niveles)
                            self.AVLTree_D.AVLinsert(nodo)
                            self.PrintInfo(nodo)

                        elif data.direccion != datadir:
                            print ("Datos no existentes, creando nuevo"+"\n")
                            nodo = Node_Celeste(datadir,fresas,caras,tiempo,muertes,niveles)
                            self.AVLTree_D.AVLinsert(nodo)
                            self.PrintInfo(nodo)
                        else:
                            print ("Datos encontrados, actualizando..."+"\n")
                            print("Datos Anteriores: "+"\n")
                            self.PrintInfo(data)
                            print("\n"+"Datos Actualizados: "+"\n")
                            data.fresas = fresas
                            data.caras = caras
                            data.tiempo = tiempo
                            data.muertes = muertes
                            data.niveles = niveles
                            self.PrintInfo(data)
                            
                    else:
                        self.AVLDict_D = self.tmp_D.InOrderTrav_Dict(self.AVLTree_D.root,self.AVLDict_D)
                        self.tmp_D.SaveTree(self.AVLDict_D)
                        break
                    
            elif menu1 == "jump king" or menu1 == "jk":
                while True:
                    choise = input("\n"+"Que desea hacer:"+"\n"+"1.Ver datos de juego"+"\n"+"2.Actualizar datos"+"\n"+"Ingrese cualquier cosa para volver"+"\n"+"\n")
                    if choise == "1":
                        datadir="JumpKing_"+ self.usercode
                        data = self.AVLTree_D.find(self.AVLTree_D.root,datadir)
                        if data == None:
                            print("Datos no existentes"+"\n")
                        elif data.direccion != datadir:
                            print ("Datos no existentes"+"\n")
                        else:
                            self.PrintInfo(data)
                        
                    elif choise == "2":
                        datadir="JumpKing_"+ self.usercode
                        muertes= str(input("muertes =  "))
                        saltos= str(input("saltos =  "))
                        tiempo= str(input("tiempo =  "))
                        data = self.AVLTree_D.find(self.AVLTree_D.root,datadir)
                        if data == None:
                            print("Datos no existentes, creando nuevo"+"\n")
                            nodo = Node_JumpKing(datadir,muertes,saltos,tiempo)
                            self.AVLTree_D.AVLinsert(nodo)
                            self.PrintInfo(nodo)

                        elif data.direccion != datadir:
                            print ("Datos no existentes, creando nuevo"+"\n")
                            nodo = Node_JumpKing(datadir,muertes,saltos,tiempo)
                            self.AVLTree_D.AVLinsert(nodo)
                            self.PrintInfo(nodo)
                        else:
                            print ("Datos encontrados, actualizando..."+"\n")
                            print("Datos Anteriores: "+"\n")
                            self.PrintInfo(data)
                            print("\n"+"Datos Actualizados: "+"\n")
                            data.muertes = muertes
                            data.saltos = saltos
                            data.tiempo = tiempo
                            self.PrintInfo(data)
                            
                    else:
                        self.AVLDict_D = self.tmp_D.InOrderTrav_Dict(self.AVLTree_D.root,self.AVLDict_D)
                        self.tmp_D.SaveTree(self.AVLDict_D)
                        break
                
            elif menu1 == "ror2":
                
                while True:
                    choise = input("\n"+"Que desea hacer:"+"\n"+"1.Ver datos de juego"+"\n"+"2.Actualizar datos"+"\n"+"Ingrese cualquier cosa para volver"+"\n"+"\n")
                    if choise == "1":
                        datadir="RoR2_"+ self.usercode
                        data = self.AVLTree_D.find(self.AVLTree_D.root,datadir)
                        if data == None:
                            print("Datos no existentes"+"\n")
                        elif data.direccion != datadir:
                            print ("Datos no existentes"+"\n")
                        else:
                            self.PrintInfo(data)
                        
                    elif choise == "2":
                        datadir="RoR2_"+ self.usercode
                        partidaML = str(input("Partida más larga =  "))
                        masFases= str(input("Mayor numero de fases =  "))
                        mayorNivel= str(input("Mayor nivel alcanzado =  "))
                        muertes= str(input("Muertes =  "))
                        victorias= str(input("Victorias =  "))
                        totalP= str(input("Total de partidas =  "))
                        data = self.AVLTree_D.find(self.AVLTree_D.root,datadir)
                        if data == None:
                            print("Datos no existentes, creando nuevo"+"\n")
                            nodo = Node_RoR2(datadir,partidaML,masFases,mayorNivel,muertes,victorias,totalP)
                            self.AVLTree_D.AVLinsert(nodo)
                            self.PrintInfo(nodo)

                        elif data.direccion != datadir:
                            print ("Datos no existentes, creando nuevo"+"\n")
                            nodo = Node_RoR2(datadir,partidaML,masFases,mayorNivel,muertes,victorias,totalP)
                            self.AVLTree_D.AVLinsert(nodo)
                            self.PrintInfo(nodo)
                        else:
                            print ("Datos encontrados, actualizando..."+"\n")
                            print("Datos Anteriores: "+"\n")
                            self.PrintInfo(data)
                            print("\n"+"Datos Actualizados: "+"\n")
                            data.partidaML = partidaML
                            data.masFases = masFases 
                            data.mayorNivel= mayorNivel
                            data.muertes = muertes
                            data.victorias = victorias
                            data.totalP = totalP
                            self.PrintInfo(data)
                            
                    else:
                        self.AVLDict_D = self.tmp_D.InOrderTrav_Dict(self.AVLTree_D.root,self.AVLDict_D)
                        self.tmp_D.SaveTree(self.AVLDict_D)
                        break
                
            else:
                print("Esa opción no esta listada, se retornará al menú de login")
                self.usercode = None
                self.AVLDict_D = self.tmp_D.InOrderTrav_Dict(self.AVLTree_D.root,self.AVLDict_D)
                self.tmp_D.SaveTree(self.AVLDict_D)

    def PrintInfo(self,node):
        print("Datos encontrados:"
        +"\n"+
        "--------------------------------"
        )
        node.PrintNode()
        print(
        "--------------------------------"   
        )

if __name__ == '__main__':
    interfaz = CmdUI()

'''
def func():
    arbol = ArbolAVL()
    doc = open("scr\Datos\data.txt","r")
    lista = doc.readlines()
    doc.close()
    start = time.perf_counter()
    for i in range(0,len(lista)):
        nodo = Node(lista[i])
        arbol.AVLinsert(nodo)
    total = time.perf_counter()-start
    print(total)
    start = time.perf_counter()
    arbol.find(arbol.root,"!")
    total = time.perf_counter()-start
    print(total)
#func()


#profile.run(func())
doc = open("scr\Datos\hashtest\data1.txt","r")
lista = doc.readlines()
doc.close()

def func1():
    tmp_P = NodeBuilder("scr\Datos\ArbolPrueba.json")
    start = time.perf_counter()
    AVLDict_P = tmp_P.ReadTree()
    AVLTree_P = tmp_P.ReconstructTree(AVLDict_P)
    total = time.perf_counter()-start
    print("DIC TO AVL = " + str(total))

    start = time.perf_counter()
    for i in range(0,len(lista)):
        datadir="JumpKing_"+lista[i]
        nodo = Node_JumpKing(datadir,0,0,0)
        AVLTree_P.AVLinsert(nodo)
    total = time.perf_counter()-start
    print("Insert Arbol = "+str(total))
    start = time.perf_counter()
    AVLTree_P.find(AVLTree_P.root,"1")
    total = time.perf_counter()-start
    print("Find = " + str(total))

    start = time.perf_counter()
    AVLDict_P = tmp_P.InOrderTrav_Dict(AVLTree_P.root,AVLDict_P)
    total = time.perf_counter()-start
    print("AVL TO DIC = " + str(total))
    tmp_P.SaveTree(AVLDict_P)
func1()


num = int(input())
arbol = ArbolAVL()
start = time.perf_counter()
for i in range(0,num):
    dat = input()
    print(i)
    nodo = Node(dat)
    arbol.AVLinsert(nodo)
total = time.perf_counter()-start
print(total)
'''