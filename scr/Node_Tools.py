from abc import ABC, abstractmethod
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None
        pass

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
                
