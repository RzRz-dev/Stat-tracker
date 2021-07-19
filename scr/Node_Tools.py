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


class Node:
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
    def __init__(self, dire,u,p):
        super().__init__(dire)
        self.username = u
        self.password = p
    def PrintNode(self):
        print(
            "Username:  "+str(self.username)+"\n"+ 
            "Password:  "+str(self.password)+"\n"
        )

class Node_Celeste(Node):
    def __init__(self, dire,f,c,t,m,n):
        super().__init__(dire)
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
    def __init__(self, dire,m,s,t):
        super().__init__(dire)
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
    def __init__(self, dire,pml,mf,mn,m,v,tp):
        super().__init__(dire)
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
        new_node = Node(data)
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
class ArbolAVL:
    def __init__(self):
        self.root = None

    def printAVL(self):
        if self.root != None:
            self.InOrderTrav(self.root)
            print("-------------------------------")
            #self.PreOrderTrav(self.root)
            print("-------------------------------")
            #self.PostOrderTrav(self.root)
        else:
            print("\n" + "llene el arbol primero" + "\n")

    def AVLinsert(self, nodo_gen):
        self.insert(nodo_gen)
        N = self.find(self.root, nodo_gen.direccion)
        self.rebalance(N)

    def AVLdelete(self,dire):
        N = self.find(self.root, dire)
        self.Delete(N)

    def LeerNodo(self, nodo):
        dir = nodo.direccion if (nodo.direccion != None) else None
        par = nodo.parent.direccion if (nodo.parent != None) else None
        r = nodo.rightSon.direccion if (nodo.rightSon != None) else None
        d = nodo.leftSon.direccion if (nodo.leftSon != None) else None
        sig = nodo.parent_signal if (nodo.parent_signal != None) else None
        h= nodo.nodeHeight
        print("nodo =" + str(dir) + "  parent =" + str(par) + "  Left =" + str(d) + "  Right=" + str(r) + "  signal=" + str(sig) +"  altura="+str(h)+ "\n")

    def insert(self, node_gen):
        node = node_gen
        if self.root == None:
            self.root = node
        else:
            parent = self.root
            while True:
                if node.direccion < parent.direccion:
                    if parent.leftSon != None:
                        parent = parent.leftSon
                    else:
                        node.parent = parent
                        node.parent_signal = "L"
                        parent.leftSon = node
                        break
                elif node.direccion > parent.direccion:
                    if parent.rightSon != None:
                        parent = parent.rightSon
                    else:
                        node.parent = parent
                        node.parent_signal = "R"
                        parent.rightSon = node
                        break
                else:
                    return "existe"

    def find(self, root, dat):
        if root == None:
            return
        self.Parent_asigner(root)
        if root.direccion == dat:
            return root
        elif root.direccion < dat:
            if root.rightSon != None:
                return self.find(root.rightSon, dat)
            return root
        elif root.direccion > dat:
            if root.leftSon != None:
                return self.find(root.leftSon, dat)
            return root

    def SingleRotation_L(self, node):
        tmp = node.rightSon
        node.rightSon = tmp.leftSon
        tmp.leftSon = node
        if node.parent == None:
            node.parent = tmp
            tmp.parent = None
            self.root = tmp
        else:
            tmp.parent = node.parent
            node.parent = tmp
        self.adjustH(node)
        self.adjustH(tmp)
        self.Parent_asigner(tmp)
        return tmp

    def SingleRotation_R(self, node):
        tmp = node.leftSon
        node.leftSon = tmp.rightSon
        tmp.rightSon = node
        if node.parent == None:
            node.parent = tmp
            tmp.parent = None
            self.root = tmp
        else:
            tmp.parent = node.parent
            node.parent = tmp
        self.adjustH(node)
        self.adjustH(tmp)
        self.Parent_asigner(tmp)
        return tmp

    def Parent_asigner(self, node):
        if node.parent == None:
            node.parent_signal = None
        if node.rightSon != None:
            node.rightSon.parent_signal = "R"
            node.rightSon.parent = node
        if node.leftSon != None:
            node.leftSon.parent_signal = "L"
            node.leftSon.parent = node

    def DoubleRotation_L(self, node):
        node.leftSon = self.SingleRotation_L(node.leftSon)
        tmp_signal_1 = node.parent_signal
        tmp_signal_2 = node.leftSon.parent_signal
        new_node = self.SingleRotation_R(node)
        new_node.parent_signal = tmp_signal_1
        new_node.leftSon.parent_signal = tmp_signal_2
        return new_node

    def DoubleRotation_R(self, node):
        node.rightSon = self.SingleRotation_R(node.rightSon)
        tmp_signal_1 = node.parent_signal
        tmp_signal_2 = node.rightSon.parent_signal
        new_node = self.SingleRotation_L(node)
        new_node.parent_signal = tmp_signal_1
        new_node.leftSon.parent_signal = tmp_signal_2
        return new_node

    def rebalance(self, node):
        parent = node.parent
        self.adjustH(node)
        h_Right = (node.rightSon.nodeHeight if
                   (node.rightSon is not None) else 0)
        h_Left = (node.leftSon.nodeHeight if (node.leftSon is not None) else 0)
        if abs(h_Left - h_Right) > 1:
            if parent == None:
                if h_Left > h_Right:
                    if node.leftSon != None:
                        h_Right = (node.leftSon.rightSon.nodeHeight if
                                   (node.leftSon.rightSon is not None) else 0)
                        h_Left = (node.leftSon.leftSon.nodeHeight if
                                  (node.leftSon.leftSon is not None) else 0)
                        if (h_Left > h_Right):
                            self.root = self.SingleRotation_R(node)
                        else:
                            self.root = self.DoubleRotation_L(node)
                else:
                    if node.rightSon != None:
                        h_Right = (node.rightSon.rightSon.nodeHeight if
                                   (node.rightSon.rightSon is not None) else 0)
                        h_Left = (node.rightSon.leftSon.nodeHeight if
                                  (node.rightSon.leftSon is not None) else 0)
                        if (h_Left > h_Right):
                            self.root = self.DoubleRotation_R(node)
                        else:
                            self.root = self.SingleRotation_L(node)
            else:
                if h_Left > h_Right:
                    if node.leftSon != None:
                        h_Right = (node.leftSon.rightSon.nodeHeight if
                                   (node.leftSon.rightSon is not None) else 0)
                        h_Left = (node.leftSon.leftSon.nodeHeight if
                                  (node.leftSon.leftSon is not None) else 0)
                        if (h_Left > h_Right):
                            if node.parent_signal == "R":
                                parent.rightSon = self.SingleRotation_R(node)
                            elif node.parent_signal == "L":
                                parent.leftSon = self.SingleRotation_R(node)
                        else:
                            if node.parent_signal == "R":
                                parent.rightSon = self.DoubleRotation_L(node)
                            elif node.parent_signal == "L":
                                parent.leftSon = self.DoubleRotation_L(node)
                else:
                    if node.rightSon != None:
                        h_Right = (node.rightSon.rightSon.nodeHeight if
                                   (node.rightSon.rightSon is not None) else 0)
                        h_Left = (node.rightSon.leftSon.nodeHeight if
                                  (node.rightSon.leftSon is not None) else 0)
                        if (h_Left > h_Right):
                            if node.parent_signal == "R":
                                parent.rightSon = self.DoubleRotation_R(node)
                            elif node.parent_signal == "L":
                                parent.leftSon = self.DoubleRotation_R(node)
                        else:
                            if node.parent_signal == "R":
                                parent.rightSon = self.SingleRotation_L(node)
                            elif node.parent_signal == "L":
                                parent.leftSon = self.SingleRotation_L(node)
        self.Parent_asigner(node)
        if parent != None:
            self.rebalance(parent)

    def adjustH(self, node):
        rh = (node.rightSon.nodeHeight if (node.rightSon is not None) else 0)
        lh = (node.leftSon.nodeHeight if (node.leftSon is not None) else 0)
        node.nodeHeight = 1 + max(lh, rh)

    def InOrderTrav(self, tree):
        if tree == None:
            return
        self.InOrderTrav(tree.leftSon)
        print(tree.direccion)
        self.LeerNodo(tree)
        self.InOrderTrav(tree.rightSon)

    def PreOrderTrav(self, tree):
        if tree == None:
            return
        print(
            str(tree.direccion) + "          altura: " + str(tree.nodeHeight) +
            "\n")
        self.PreOrderTrav(tree.leftSon)
        self.PreOrderTrav(tree.rightSon)

    def PostOrderTrav(self, tree):
        if tree == None:
            return
        self.PostOrderTrav(tree.leftSon)
        self.PostOrderTrav(tree.rightSon)
        print(
            str(tree.direccion) + "          altura: " + str(tree.nodeHeight) +
            "\n")

    def nextNode(self, node):
        if node.rightSon != None:
            return self.LeftDes(node.rightSon)
        else:
            return self.RightAns(node)

    def LeftDes(self, node):
        if node.leftSon == None:
            return node
        else:
            self.LeftDes(node.leftSon)

    def RightAns(self, node):
        if node.parent != None:
            if node.direccion < node.parent.direccion:
                return node.parent
            else:
                return self.RightAns(node.parent)
        else:
            return node

    def Delete(self, node):
        if node.leftSon == None and node.rightSon == None:
            tmp=node.parent
            if node.parent_signal == "R":
                node.parent.rightSon = None
                node.parent = None
            elif node.parent_signal == "L":
                node.parent.leftSon = None
                node.parent = None
            if self.root == node:
                self.root = None
            if tmp != None:
              self.rebalance(tmp)
        elif node.leftSon == None or node.rightSon == None:
            if node.leftSon != None:
                tmp=node.leftSon
                node.direccion=tmp.direccion
                node.tipo=tmp.tipo
                node.area=tmp.area
                self.Delete(node.leftSon)
            else:
                tmp=node.rightSon
                node.direccion=tmp.direccion
                node.tipo=tmp.tipo
                node.area=tmp.area
                self.Delete(node.rightSon)
                self.LeerNodo(self.root)
        else:
            sucesor = self.nextNode(node)
            node.direccion=sucesor.direccion
            node.tipo=sucesor.tipo
            node.area=sucesor.area
            self.Delete(sucesor)
                
