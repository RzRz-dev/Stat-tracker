from abc import ABC, abstractmethod
import json
"""
#Leer arbol
tf = open("scr\Datos\ArbolAVL.json", "r")
dict_arbol = json.load(tf)

#Guardar arbol
tf = open("scr\Datos\ArbolAVL.json", "w")
json.dump(general,tf)
tf.close()
"""
class ChainNode:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None
class Node:
    def __init__(self):
        self.next = None
class TreeNode:
    def __init__(self, dire):
        self.direccion = dire
        self.parent = None
        self.parent_signal = None
        self.rightSon = None
        self.leftSon = None
        self.nodeHeight = 0
        pass
    '''
    self.data = data
    self.next = None
    self.back = None
    pass
    '''
class Node_User(Node):
    def __init__(self,id,p):
        super().__init__()
        self.ID = id
        self.password = p
    def PrintNode(self):
        print(
            "Username:  "+str(self.username)+"\n"+ 
            "Password:  "+str(self.password)+"\n"
        )

class Node_Celeste(Node):
    def __init__(self,f,c,t,m,n):
        super().__init__()
        self.fresas = f
        self.caras= c
        self.tiempo= t
        self.muertes= m
        self.niveles= n

    def PrintNode(self):
        print(
            "Fresas:  "+str(self.fresas)+"\n"+ 
            "Caras:  "+str(self.caras)+"\n"+
            "Tiempo:  "+str(self.tiempo)+"\n"+
            "Muertes:  "+str(self.muertes)+"\n"+
            "Niveles:  "+str(self.niveles)+"\n"
        )

class Node_JumpKing(Node):
    def __init__(self,m,s,t):
        super().__init__()
        self.muertes = m
        self.saltos = s
        self.tiempo =t

    def PrintNode(self):
        print(
            "Muertes:  "+str(self.muertes)+"\n"+ 
            "Saltos:  "+str(self.saltos)+"\n"+
            "Tiempo:  "+str(self.tiempo)+"\n"
        )
        
class Node_RoR2(Node):
    def __init__(self,pml,mf,mn,m,v,tp):
        super().__init__()
        self.partidaML = pml
        self.masFases = mf
        self.mayorNivel = mn
        self.muertes = m
        self.victorias = v
        self.totalP = tp
    def PrintNode(self):
        print(
            "Partida más larga:  "+str(self.partidaML)+"\n"+ 
            "Mayor numero de fases:  "+str(self.masFases)+"\n"+
            "Mayor nivel alcanzado:  "+str(self.mayorNivel)+"\n"+
            "Muertes:  "+str(self.muertes)+"\n"+
            "Victorias:  "+str(self.victorias)+"\n"+
            "Total de partidas:  "+str(self.totalP)+"\n"
        )

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        #self.first_gnode = None

    def insert_at_end(self, data):
        new_node = TreeNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node.back = n
        n.next = new_node
        self.tail = new_node
        
    def traverse_list(self):
        if self.head == None:
            print("Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next


class HashBuilder:

    def SaveData(self,src,mapa):
        tmplist= self.ReadList(mapa.array)
        with open(src, 'w') as filehandle:
            json.dump(tmplist, filehandle)
        filehandle.close()

    def ReadData(self,src,mapa):
        with open(src, 'r') as filehandle:
            data_json = json.load(filehandle)
        mapa.array= self.WriteList(data_json)
        filehandle.close()

    def ListToNode(self,List):
        if List != None:
            if List[0] == "CN":
                head = ChainNode(List[1],List[2])
                next=List[3]
                head.next = self.ListToNode(next)
                return head
                """
            elif List[0] == "NU":
                return Node_User(List[1],List[2])
            elif List[0] == "NC":
                return Node_User(List[1],List[2],List[3],List[4],List[5])
            elif List[0] == "NJK":
                return Node_User(List[1],List[2],List[3])
            elif List[0] == "NROR":
                return Node_User(List[1],List[2],List[3],List[4],List[5],List[6]"""
        return 
        
    def WriteList(self,List):
        nlist=[]
        for i in List:
            nlist.append(self.ListToNode(i))
        return nlist

    def ReadList(self,List):
        nlist = []
        #nlist.insert(ListL)
        for i in List:
            #print(i)
            #tmp=i
            nlist.append(self.NodeToList(i))

        return nlist
                
    def NodeToList(self,node=None):
        if node != None:
            if isinstance(node,ChainNode):
                return ["CN",node.key,node.value,self.NodeToList(node.next)]
                """
            elif isinstance(node,Node_User):
                return [
                        "NU",
                        node.ID,
                        node.password
                    ]
            elif isinstance(node,Node_Celeste):
                return [
                        "NC",
                        node.fresas,   
                        node.caras,
                        node.tiempo,
                        node.muertes,
                        node.niveles
                    ]
            elif isinstance(node,Node_JumpKing):
                return [
                        "NJK",
                        node.muertes,
                        node.saltos,
                        node.tiempo
                    ]
            
            elif isinstance(node,Node_RoR2):
                return [
                    "NROR",
                    node.partidaML,
                    node.masFases,
                    node.mayorNivel,
                    node.muertes,
                    node.victorias,
                    node.totalP
                ]"""
        return

class Nmap:

    def __init__(self):
        self.array = []

    def FillArray(self,n):
        realn=n-len(self.array)+1
        tmp = [None]*realn
        self.array = self.array+tmp
        return

    def HashFunc(self,S):
        hash = 0
        tope=len(S) - 1
        for i in range(tope,-1,-1):
            hash = (hash*7 + ord(S[i]))%5316847
        return hash
        
    def HasKey(self,O):
        L = self.HashFunc(O)
        if L > (len(self.array)-1):
            return False
        head = self.array[L]
        while head != None:
            if head.key == O:
                return True
            else:
                head = head.next
        return False

    def Get(self,O):
        L=self.HashFunc(O)
        if L > (len(self.array)-1):
            return
        head=self.array[L]
        while head != None:
            if O == head.key:
                return head.value
            else:
                head=head.next
        return "NO"

    def Set(self,O,v):
        L=self.HashFunc(O)
        if len(self.array)-1 < L:
            self.FillArray(L)
            self.array[L]=ChainNode(O,v)
            #self.array[L]=[O,v,"None"]
            #self.dirData.insert(L)
            return 2
        prev=None
        head=self.array[L]
        if head == None:
            self.array[L]=ChainNode(O,v)
            #self.array[L]=[O,v,"None"]
            #self.dirData.insert(L)
            
            return 4
        else:   
            while head != None:
                if O == head.key:
                #if O == head[0]:
                    head.value = v
                    #head[1]=v
                    return 1
                
                else:
                    prev=head
                    #head=head[2]
                    head = head.next
            prev.next=ChainNode(O,v)
            #head[2]=[O,v,"None"]
            #self.dirData.insert(L)
            return 0
                
