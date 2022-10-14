from doubleLinkedListNode import DoubleLinkedListNode
from singleLinkedlist import SingleLinkedList

sll= SingleLinkedList()
dll= DoubleLinkedListNode()

class Menu:

    def menu_secundario(self, clase):
        respuesta= input('a. Añadir nodo\n  b.Eliminar nodo\n')
        if respuesta == "a" or respuesta == "b":
            accion = int(input('1.  Al inicio\n2. Al final\n3.  En una posicion especifica'))
            if accion == "a":
                if accion == 1 and isinstance(clase, sll):
                    sll.push_node()


 
    def show_menu(self):
        print("Con que tipo de listas vas a trabajar?")
        answer= int(input('1. Simplemente enlazadas\n2. Doblemente enlazadas\n3.Salir'))
        if answer == 1:
            self.menu_secundario(sll)
        elif answer ==2:
            self.menu_secundario(dll)
    
    