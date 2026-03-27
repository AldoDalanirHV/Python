import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__() #Contructor de la clase padre que es Tk
        #confoguracion de la ventana
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_tabla()
        #self.mainloop()  #Para mostrar ventana al momento de crear un objeto
        #self.estilo_de_ventana()

    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='#1d2d44')
        self.title('Manejo de ventanas con POO')

    def configurar_grid(self):
        self.columnconfigure(0,weight=1) #Aqui se muestra la tabla y aqui se configura el scrollbar
        self.columnconfigure(1, weight=0)

    # mostarr reg seleccionado

    def mostrar_registro_seleccionado(self, event):
        print(f'metodo mostrar registro seleecionado')
        elemento_select = self.tabla.selection()[0]  # Solo el primer registro seleccionado
        elemento = self.tabla.item(elemento_select)  # item=elementp
        persona = elemento['values']  # Tupla de personas
        print(f'La inf de la persona seleccionada es: {persona}')
        showinfo(title='Persona seleccionada', message=f'Inf de la persona{persona}')

    def mostrar_tabla(self):
        # estilo
        estilo = ttk.Style()
        estilo.theme_use('clam')  # prepaea el menejo del tema oscuro
        estilo.configure('Treeview', background='black',
                         foreground='white',  # color de texto
                         fieldbackground='black',  # color de fondo de la tabla
                         rowheight=30  # tamaño en pixeles de cada uno de los registros
                         )
        # al seleccionar los registros
        estilo.map('Treeview',
                   background=[('selected',  # sentencia al seleccionar algun registro
                                '#3a86ff'  # Cambia al color que queremos
                                )])

        # definir las columnas
        columnas = ('Id', 'Name', 'Age')
        self.tabla = ttk.Treeview(self , columns=columnas, #Se pasa solo el paramtro self para que cuando se creee l objeto pase como referencia ese paremtro
                             show='headings')  # Paquete que crea un componente de tabla con la tupla de valores que queremos usar
        # Headings es solo para mostrar los cabeceros no para un treeview(para sunregistros)

        # Cabeceras de tabla
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)  # Me parece que pueden ser iguales
        self.tabla.heading('Name', text='Name', anchor=tk.W)  # Para hacer a la izquierda o donde sea
        self.tabla.heading('Age', text='Age',
                      anchor=tk.W)  # Primer columna no se dezpliega ya que ahi se muestar inf ma detalle de los registros ya que es un 'Treeview'

        # Inf de tabla  -  fromato de columnas
        self.tabla.column('Id', width=80)  # Son pixeles asi que son pequeñas
        self.tabla.column('Name', width=120)
        self.tabla.column('Age', width=120)

        # Cargar datos a la tabla
        datos = ((1, 'Aldo', 24), (2, 'Daniela', 24))  # Tupla de valores

        # iterar para insertar los valores
        for persona in datos:
            self.tabla.insert(parent='', index=tk.END, values=persona)

        # CREAR UN scrollbar(DEZLIZAR) -- BARRA DE DEZPLAZAMINTO
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview) # Self=Objeto que se esta pasando en ese momento
        self.tabla.configure(yscroll=scrollbar.set)  # para sincrozinar sobre el eje la visualizacion de los registros de la tabla
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # asociar el evento select a la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)

        # Publicar tabla
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)


if __name__ == '__main__':
    app=App()
    app.mainloop()


