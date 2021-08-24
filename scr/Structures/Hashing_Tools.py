#from PyQt5.sip import array
from Node_Tools import ChainNode,Node_User
from Node_Builder import HashBuilder
import json,time

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
            hash = (hash*7 + ord(S[i]))%179
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

    def Peek(self,O):
        L=self.HashFunc(O)
        if L > (len(self.array)-1):
            return 
        head=self.array[L]
        while head != None:
            if O == head.key:
                return "EXISTE"
            else:
                head=head.next
        return "NO EXISTE"

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

if __name__ == '__main__':
    start = time.perf_counter()

    builder = HashBuilder()
    mapa = Nmap()
    doc = open("scr\Datos\data2.txt","r")
    lista = doc.read()
    doc.close()
    listaa=lista.split("_")
    nodeTest=Node_User("aaa","123")
    for i in listaa:
        mapa.Set(i,nodeTest)
    
    #print(lista[9998])
    #print(mapa.HasKey("xPONsc6BTx9g"))
    #print(mapa.HasKey("W1m9y2AymKgf"))
    #print(mapa.Get("eNlyjCHXH5P0"))
    #mapa.Set("QFo91kDjyb75","1")
    #mapa.Set("fKzWGiNnw7l5","2")
    #mapa.Set("Sz3D4f7N0GHk","3")
    #mapa.Set("eNlyjCHXH5P0","4")
    #mapa.Set("GekL3qFqO1XD","5")
    print(mapa.array)
    nlist= builder.ReadList(mapa.array)




    with open('scr\Datos\pruebas_hash.json', 'w') as filehandle:
        json.dump(nlist, filehandle)

# open output file for reading
    with open('scr\Datos\pruebas_hash.json', 'r') as filehandle:
        prueba = json.load(filehandle)

    print(prueba[-2])
    print(type(prueba[-2]))


    total = time.perf_counter()-start
    print(total)

    mapa2=Nmap()
    mapa2.array= builder.WriteList(prueba)
    print(mapa2.array[-1].key,mapa2.array[-1].value.ID)





