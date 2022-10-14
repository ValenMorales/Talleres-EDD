from multiprocessing.sharedctypes import Value


class DoubleLinkedListNode:
    class Node:
        def __init__(self, value):
            self.value =value
            self.next= None
            self.previous = None



        def print_list(self):
            array_dll =[ ]
            current_node = self.head
            while current_node is not None:
                array_dll.append(current_node.value)
                current_node = current_node.next
            return array_dll
        

        def unshift_node(self,value):
            new_node= self.Node(value)
            if self.head== None and self.tail == None:
                self. head = new_node
                self.tail= new_node
            else:
                self.head.previous = new_node
                new_node.next = self.head
                self.head = new_node 
            self.length +=1


        #eliminar primer nodo de la lista 
        def shift_node(self):
            if self.length ==0:
                self.head = None
                self.tail= None
            elif self.head != None:
                remove_node = self.head
                self.head = remove_node.next
                remove_node.next = None
                self.length -=1
                return print (remove_node.value)

        #eliminar el primer nodo de la lista 
        def shift_node (self):
            if self.length ==0:
                self.head= None
                self.tail = None
            elif self.head != None:
                remove_node = self.head 
                self.head = remove_node.next
                remove_node.next = None
                self.length -=1
                return print(remove_node.value)

        #eliminar el ultimo nodo de la lista 
        def ppop_node (self):
            if self.length ==0:
                self.head = None
                self.tail = None
            else:
                remove_node = self.tail 
                self.tail = remove_node.previous 
                self.tail.next = None
                remove_node.previous = None
                self.length -=1
                return print(remove_node.value)



