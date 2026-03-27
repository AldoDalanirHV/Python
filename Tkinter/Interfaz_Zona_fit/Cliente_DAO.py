'''Se utiliza el patron de diseño DAO Data Access Object

Que es un patron de siseño?
Son soluciones a problemas que nos encontramos conmunente al crear aplicaciones

Cada patron de diseño es como un plano que podemos usar y personalizar para resolver un problema al diseñar una aplicacion, algo asi como una plantilla

DAO  ->> DATA ACCESS OBJECT
SE UTILIZA PARA ACCEDER A INFORMACION DE UNA ENTIDAD DE NUESTRA APLICACION, EN ESTE CASO LA TABLA DE CLIENTE(DATABASE)
'''
from inspect import cleandoc

from Interfaz_Zona_fit.Conexion import Conexion
from Interfaz_Zona_fit.Cliente import Cliente

class Cliente_DAO:
    select= 'select * from Cliente order by id'
    insert='insert into Cliente (nombre, apellido, membresia) values (%s,%s,%s)'
    update='update Cliente set nombre=%s, apellido=%s, membresia=%s where id=%s'
    delete='delete from Cliente where id=%s'

    @classmethod
    def seleccionar(cls):
        conexion=None
        try:
            conexion= Conexion.obtener_conexion()
            cursor=conexion.cursor()
            cursor.execute(cls.select)
            registros=cursor.fetchall() #POR CADA REGISTROQ UE RECUPERAMOS, VAMOS A CREAR UN OBJETOS DE TIPO CLIENTE
            #MaPEO DE CLASE-TABLA CLIENTE  ---SE HACE UN MAPEO CON LA TABLA DE LA BASE DE SATOS CON LA CLASE CLIENTE
            #SE LES CONOCE COMO ORM-- OBJECT RELATIONAL MAPPING(MAPEO DE RELACION-ENTIDAD(EN ESTE CASO LA CLASE CLIENTE)
            clientes=[]
            for registro in registros:
                cliente =Cliente(registro[0], registro[1],
                                 registro[2], registro[3])
                clientes.append(cliente)
            return clientes

        except Exception as error:
            print(f'Ocurrio un error al seleccionar los cliente del tipo -->" {error} "<--')
        finally:
            if conexion is not None: #Se cierra ya que este si se utilizo por eso lo liberamos
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            cursor.execute('set session auto_increment_increment=1') #Para que los od se pongan de 1 en 1 FUNCIONA
            #Llamar a clase cliente para poder insertarlos
            valores=(cliente.nombre, cliente.apellido,cliente.membresia)
            cursor.execute(cls.insert,valores)
            conexion.commit()
            #print(f'Se a añadido correctamente el cliente')
            #return cursor.rowcount #esto es para ver cuantos registros se modificaron
        except Exception as error:
            print(f'A ocurrido un error al insertar el clinte de tipo -->" {error} "<--')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.nombre, cliente.apellido, cliente.membresia,cliente.id)
            cursor.execute(cls.update,valores)
            conexion.commit()
            #print(f'Se a modificado correctamente el usuario con ID={cliente.id}\n')
            #return cursor.rowcount  # esto es para ver cuantos registros se modificaron
        except Exception as error:
            print(f'Sucedio un error al actualizar el usuario del tipo -->" {error} "<--')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls,cliente):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.id,) #Debe ponerse " , " ya que esta indicando que la tupla hay mas valores pero vacios
            cursor.execute(cls.delete, valores)
            conexion.commit()
            # print(f'Se a eliminado correctamnete el usuario con el ID {cliente.id}')
            #return cursor.rowcount
        except Exception as error:
            print(f'Ocurrio un error al eliminar el clinete de tipo --> " {error} "<--')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__=='__main__':
    # insertar_cliente=Cliente_DAO.selection()
    # for cliente in insertar_cliente:
    #     print(cliente)
    # cliente=Cliente(nombre='Gabriel',apellido='Sanchez',membresia=200) #Se crea el objeto cliente
    # cliente_insertados=Cliente_DAO.insertar(cliente) #INSERTAMOS OBJETOS DE TIPO CLIENTE, ES INFORMACION DE OBJETOS
    # print(f'Clientes insertados {cliente_insertados}\n')
    # cliente=Cliente(58,'')
    # ver la lisa de clientes actualizadad
    client=Cliente(33)
    # update_client=Cliente_DAO.actualizar(client)
    # print(f'Clinetes actualizados {update_client}')
    delete_client=Cliente_DAO.eliminar(client)
    print(f'Clientes modificados ->{delete_client}')
    clientes=Cliente_DAO.seleccionar()
    print(f'Lista de clintes: ')
    for cliente in clientes:
        print(cliente)
