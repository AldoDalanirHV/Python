from Interfaz_Zona_fit.Cliente import Cliente
from Interfaz_Zona_fit.Cliente_DAO import Cliente_DAO

class ZonaFit:
    def __init__(self):
        self.zona_fit=Cliente_DAO()
    def menu(self):
        opcion=True
        while opcion is not False:
            try:
                print(f'''Menu
                1-°Ver Clientes
                2-°Insertar nuevo Cliente
                3-°Actualizar datos clinte
                4-°Eliminar cliente
                5- Salir°''')
                opcion=int(input(f'Ingresa el lo que deseas hacer:'))
                opcion=self.realizar_accion(opcion)
            except Exception as error:
                print(f'A ocurrido un error del tipo ->" {error} "<-')
    def realizar_accion(self,opcion):
        if opcion ==1:
            self.ver_cliente()
        elif opcion ==2:
            self.insertar_cliente()
        elif opcion == 3:
            self.actualizar_cliente()
        elif opcion ==4:
            self.eliminar_cliente()
        elif opcion ==5:
            print(f'Hasta pronto!!!!')
            return False
        else:
            print(f'Ingresa una opcion valida')

    def ver_cliente(self):
        mostrar_cliente=Cliente_DAO.seleccionar()
        print(f'Aqui estan la lista de los clientes mostrados\n')
        for cliente in mostrar_cliente:
            print(cliente)
    def insertar_cliente(self):
        name=input(f'Ingresa el nombre del cliente a ingresar: ')
        last_name=input(f'Ingresa el apellido del cliente a ingresar: ')
        membresia=int(input(f'Ingresa el numero de membresia: '))
        cliente=Cliente(nombre=name,apellido=last_name,membresia=membresia) #Creamo el objeto de tipo clinente
        print(f'# de clientes añadidos {self.zona_fit.insertar(cliente)}')#Pasamos ese objeto a insertar y mostramos el #de clientes actualizados en la base de datos
    def actualizar_cliente(self):
        name = input(f'Ingresa el nombre del cliente a ingresar: ')
        last_name = input(f'Ingresa el apellido del cliente a ingresar: ')
        membresia = int(input(f'Ingresa el numero de membresia: '))
        id=int(input(f'Ingresa el Id del cliente a actualizar: '))
        cliente=Cliente(id,name,last_name,membresia)
        print(f'# de clientes actualizados {self.zona_fit.actualizar(cliente)}')
    def eliminar_cliente(self):
        id=int(input(f'Ingresa el id del cliente a eliminar: '))
        cliente=Cliente(id)
        print(f'# de clientes eliminados {self.zona_fit.eliminar(cliente)}')
if __name__ == '__main__':
    cliente=ZonaFit().menu()
