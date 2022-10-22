from contextlib import nullcontext

class SingleLinkedList:
    class node:
        def __init__(self,value):
            self.value=value
            self.next=None
    def __init__(self):
        self.head= None
        self.tail= None
        self.length=0



    def show_info(self):
        print_sll= [ ]
        current_node =self.head
        while current_node != None:
            print_sll.append(current_node.value)
            current_node=current_node.next
        print(f'lista resultante: {print_sll}, cantidad de nodos {self.length}')

#pone un nodo al final de la lista
    def push_node(self, value): 
        if self.exists(value)== False:
            new_node=self.node(value)
            if self.head == None:
                self.head= new_node
                self.tail=new_node
            else:
                self.tail.next=new_node # se genera el enlace (algo como crear un nodo vacio para despues darle valor)
                self.tail=new_node      #al nodo que se "creo" anteriormente se le asigna el valor del nodo que llega como parametro a la funcion
            self.length+=1
    


    def unshift_node(self, value):#pone un nodo al principio de la lista
        if self.exists(value)== False:
            new_node=self.node(value)

            if self.head==None and self.tail==None:
                self.head=new_node
                self.tail=new_node 
            else:
                new_node.next=self.head #enlazo el nuevo nodo con la cabeza de la lista 
                self.head=new_node #y ahora la cabeza pasa a ser el nuevo nodo
            self.length+=1
    

    #eliminar nodo al inicio de la lista
    def shift_node(self):
        if self.length ==0:
            self.head =None
            self.tail= None
        else:
            #actualizamos el nombre de la cabeza con la var aux remove_node
            remove_node= self.head
            #actualizamos la cabeza de la lista
            self.head= remove_node.next
            #eliminamos el enlace de remove_node con la lista
            remove_node.next= None
            self.length -=1


#borrar el ultimo nodo de la lista 
    def pop_node(self):
        if self.length ==0 or self.length == 1:
            self.head = None
            self.tail= None
            self.length=0
        else:
            current_node = self.head
            #cuando llega al nodo que actualmente es la cola de la lista
            #no ingresa
            while current_node != None:
                new_tail = current_node
                current_node=current_node.next
            #desvinculamos la cola anterior de la lista 
            self.tail= new_tail
            new_tail.next= None
            self.tail.next= None
            self.length -=1


    def get_node(self, index):
        while True:
            if index == self.length-1:
                return self.tail
            elif index==0:
                return self.head

            elif index <0 or index >= self.length:
                return None
            else:
                current_node = self.head
                contador=0
                while index != contador:
                    current_node = current_node.next
                    contador+=1
                return current_node
        
    
    def get_node_value(self, index):
        while True:
            if index == self.length-1:
                return self.tail.value
            elif index==0:
                return self.head.value

            elif index <0 or index >= self.length:
                return None
            else:
                current_node = self.head
                contador=0
                while index != contador:
                    current_node = current_node.next
                    contador+=1
                return current_node.value
    
    #modificar valor de un nodo 
    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            #encontro el valor y se puede actualizar 
            search_node.value= int(new_value)
        else:
            print('no se encontro el nodo a buscar ')
            return None

    def remove_node(self, index):
        if index == 1:
            self.shift_node()
        elif index == self.length:
            self.pop_node()
        else:
            remove_node = self.get_node(index)
            if remove_node!= None:
                previous_node = self.get_node(index - 1)
                previous_node.next = remove_node.next
                remove_node.next = None
                self.length-=1


    def insert_node(self, index, value):
        if self.exists(value) == False:
            if index < 1 or index > self.length+1:
                print('posicion erronea')
            elif index == 1:
                self.unshift_node(value)
            elif index == self.length+1:
                self.push_node(value)
            else:
                previous_node = self.get_node(index-1)
                new_node = self.node(value)
                next_node = previous_node.next
                previous_node.next = new_node
                new_node.next = next_node
            self.length +=1


    def reverse_node(self):
        current_node = self.head
        previous_node = None
        while current_node != None:
            next_node= current_node.next
            current_node.next= previous_node
            previous_node= current_node
            current_node= next_node
        self.head= previous_node
    

    def exists(self,value):
        bandera = False
        if self.length == 1:
            valor= self.get_node_value(0)
            if int(valor) == int(value):
                bandera= True
                print('posicion existente')
        for i in range (self.length-1):
            if self.get_node_value(i) != None:
                if int(self.get_node_value(i))== int(value):
                    bandera = True 
                    print('posicion existente')
        return bandera 
         
         

    

