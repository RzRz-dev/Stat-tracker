from Node_Tools import Node_User,Node_Celeste,Node_JumpKing,Node_RoR2,ArbolAVL
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
'''
prueba=Node_JumpKing("JumpKing_7e240de74fb1ed08fa08d38063f6a6a91462a815","10","11","12")
nod=Node_User("User_7e240de74fb1ed08fa08d38063f6a6a91462a815","A","B")
nod2=Node_User("User_7e240de74fb1ed08fa08d38063f6a6a91472a815","X","Y")
x = nod.direccion
x = x.split("_")
Builder= NodeBuilder()
general={}
general = Builder.DeconstructNode(nod,general)
general = Builder.DeconstructNode(nod2,general)
general = Builder.DeconstructNode(prueba,general)
'''
