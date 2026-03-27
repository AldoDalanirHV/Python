#Pool de conexiones
'''Objetos de conexion listos para usarse, se usan en vez de crear un objeto de tipo conexion, al termianr de usarse el objeto se libera
para que otro usuario pueda usarlo, esto es mejor para menjor manejo de memoria y procesador'''

from mysql.connector import pooling
from mysql.connector import Error

#POOL DE CONEXIONES
class Conexion:
    database = 'ZonaFit'
    username =  'Practica'
    password= '123456'
    port='3306'
    host='localhost'
    pool_zise=5
    pool_name= 'Zona_fit_pool'
    pool=None

    @classmethod
    def obtener_pool(cls): #se crea el pool
        if cls.pool is None: #se condiciona si ya o no se creo el pool
            try:
                cls.pool=pooling.MySQLConnectionPool(
                    pool_name=cls.pool_name,
                    pool_size=cls.pool_zise,
                    host=cls.host,
                    port=cls.port,
                    database=cls.database,
                    user=cls.username,
                    password=cls.password
                )
                return cls.pool
            except Error as error:
                print(f'Ocurrio un error con el pool de conexiones del tipo -->{error}<--')
        else: #Si ya existe solo se retorna el Pool existente
            return cls.pool

    @classmethod
    def obtener_conexion(cls): #
        return cls.obtener_pool().get_connection() #le pedimos un objeto de tipo conexion
    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close() #Se libera eel objeto y se regrese al pool de conexiones

if __name__ == '__main__':
    pool=Conexion().obtener_pool()
    print(pool)
    conexion1=pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'se a liberado el objeto conexion 1')