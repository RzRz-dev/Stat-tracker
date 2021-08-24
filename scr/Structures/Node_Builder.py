from Node_Tools import Node_User,Node_Celeste,Node_JumpKing,Node_RoR2,ArbolAVL,ChainNode
import json

class NodeBuilder ():
    def __init__(self,doc):
        self.infoDoc = doc
    
    def InOrderTrav_Dict(self, tree, gDict):
        if tree == None:
            return
        self.InOrderTrav_Dict(tree.leftSon,gDict)
        gDict=self.DeconstructNode(tree,gDict)
        self.InOrderTrav_Dict(tree.rightSon,gDict)
        return gDict
        
    def SaveTree(self,gDict):
        tf = open(self.infoDoc, "w")
        json.dump(gDict,tf)
        tf.close()

    def ReadTree(self):
        tf = open(self.infoDoc, "r")
        try:
            dict_wrapped = json.load(tf)
        except:
            dict_wrapped = {}
        tf.close()
        return dict_wrapped

    def ReconstructTree(self,bDict):
        arbol = ArbolAVL()
        for keys in bDict:
            lista=bDict[keys]
            tmp_1=str(keys)
            tmp = tmp_1.split("_")
            if tmp[0]=="Celeste":
                nodo=Node_Celeste(tmp_1,lista["fresas"],lista["caras"],lista["tiempo"],lista["muertes"],lista["niveles"])
            elif tmp[0]=="User":
                nodo=Node_User(tmp_1,lista["usern"],lista["passw"])
            elif tmp[0]=="JumpKing":
                nodo = Node_JumpKing(tmp_1,lista["muertes"],lista["saltos"],lista["tiempo"])
            elif tmp[0]=="RoR2":
                nodo = Node_RoR2(tmp_1,lista["partidaML"],lista["masFases"],lista["mayorNivel"],lista["muertes"],lista["victorias"],lista["totalP"])
            arbol.AVLinsert(nodo)
        return arbol


    def DeconstructNode(self,node,nDict):
        iDict={}
        tmp = node.direccion.split("_")
        if tmp[0] == "User":
            iDict.update(usern = str(node.username),
                passw = str(node.password)
            )
        elif tmp[0] == "Celeste":
            iDict.update(fresas = str(node.fresas),
            caras = str(node.caras),
            tiempo = str(node.tiempo),
            muertes = str(node.muertes),
            niveles = str(node.niveles)
        )
        elif tmp[0] == "JumpKing":
            iDict.update(muertes = str(node.muertes),
            saltos = str(node.saltos),
            tiempo = str(node.tiempo)
        )
        elif tmp[0] == "RoR2":
            iDict.update(partidaML = str(node.partidaML),
            masFases = str(node.masFases),
            mayorNivel = str(node.mayorNivel),
            muertes = str(node.muertes),
            victorias = str(node.victorias),
            totalP = str(node.totalP)
        )
        else:
            print ("codigo no valido")
            return

        tmp=str(node.direccion)
        exec("nDict.update("+str(node.direccion)+"= iDict)")
        return nDict

class HashBuilder:

    def ListToNode(self,List):
        if List != None:
            if List[0] == "CN":
                head = ChainNode(List[1],self.ListToNode(List[2]))
                next=List[3]
                head.next = self.ListToNode(next)
                return head
            elif List[0] == "NU":
                return Node_User(List[1],List[2])
            elif List[0] == "NC":
                return Node_User(List[1],List[2],List[3],List[4],List[5])
            elif List[0] == "NJK":
                return Node_User(List[1],List[2],List[3])
            elif List[0] == "NROR":
                return Node_User(List[1],List[2],List[3],List[4],List[5],List[6])
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
                return ["CN",node.key,self.NodeToList(node.value),self.NodeToList(node.next)]
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
                ]
        return
#n=Node_User(1,2)


