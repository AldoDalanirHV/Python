class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id= id
        self.nombre=nombre
        self.apellido=apellido
        self.membresia=membresia

    def __str__(self): #Se usa para inprimir el estado de este objeto
        # return f'Id:{ self.id} - Nombre:{self.nombre} - Apellido: {self.apellido} - Membresia:{self.membresia}'
        return f'{self.id}  {self.nombre}  {self.apellido} {self.membresia}'

if __name__ == '__main__':
    cliente=Cliente(154, 'Aldo', 'Dalanir', 100)
    print(cliente.id)