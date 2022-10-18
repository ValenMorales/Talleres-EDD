from doubleLinkedListNode import DoubleLinkedListNode
from singleLinkedlist import SingleLinkedList

sll= SingleLinkedList()
dll= DoubleLinkedListNode()

class Menu:

    def do_insert_options(self, accion, clase):
        valor= int(input('indica el valor del nodo a agregar '))
        if accion == 1:

            clase.unshift_node(valor)
        elif accion == 2:
            clase.push_node(valor)
        elif accion == 3:
            index= int(input('En que posicion quieres añadir el nodo?'))
            clase.insert_node(index, valor)
        else:
            print('ingresa un valor valido')
        clase.show_info()

    def do_delete_options(self,accion, clase):
        if accion == 1:
            clase.shift_node()
        if accion == 2:
            clase.pop_node()
        if accion== 3:
            index= int(input('En que posicion quieres eliminar el nodo?'))
            clase.remove_node(index)


    def menu_secundario(self, clase):
        print('Indica una accion')
        print ('a. Añadir nodo\nb.Eliminar nodo\nc.Consultar valor contenido en el nodo\nd.Modificar valor de nodo\ne.Invertir toda la lista')
        if isinstance(clase, SingleLinkedList):
            respuesta= input('\n')
        if isinstance(clase, DoubleLinkedListNode):
            respuesta= input('f.Validacion especial\n')
        if respuesta == "a" or respuesta == "b":
            accion = int(input('1.  Al inicio\n2.   Al final\n3.  En una posicion especifica\n'))
            if respuesta == "a":
                self.do_insert_options(accion, clase)
            if respuesta == "b":
                self.do_delete_options(accion, clase)
        if respuesta == "c":
            index= int(input('de que posicion necesitas saber el valor?'))
            print(clase.get_node_value(index))
        if respuesta== "d":
            index= int(input('de que posicion necesitas modificar el valor?'))
            valor= input('indica el nuevo valor')
            clase.update_node_value(index, valor)
        if respuesta == "e":
            clase.reverse_node()
        if respuesta == "f" and isinstance(clase, DoubleLinkedListNode):
            index= int(input('en que posicion vas a insertar el valor?'))
            valor= input('indica el nuevo valor')
            dll.special_validation(index, valor)
        clase.show_info()



 
    def show_menu(self):
        while True:
            print("Con que tipo de listas vas a trabajar?")
            answer= int(input('1. Simplemente enlazadas\n2. Doblemente enlazadas\n3.Salir\n'))
            if answer >= 1 and answer <=3:
                if answer == 1:
                    self.menu_secundario(sll)
                elif answer ==2:
                    self.menu_secundario(dll)
                else:
                    break

    



            
            
            
            


            






