import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from Interfaz_Zona_fit.Cliente import Cliente
from Interfaz_Zona_fit.Cliente_DAO import Cliente_DAO

class App(tk.Tk):
    def __init__(self): #Constructor
        self.zona_fit=Cliente_DAO()
        #Configuracion de la clase de la ventana
        super().__init__() #Constructor de la clase padre que es Tk
        self.window_conf()
        self.grid_conf()
        self.styles()
        self.show_form()
        self.show_table()
        self.db_date_in_table()
        self.show_buttons()
        self.Events()

    def window_conf(self):
        self.geometry('900x500')
        self.title('Zona Fit')
        self.configure(background='#1d2d44')

    def grid_conf(self):
        #Columnas
        self.columnconfigure(0, weight=1) #Columna de formulario
        self.columnconfigure(1, weight=1) #Columna de tabla
        #Filas
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1) #fila formulario y tabla
        self.rowconfigure(2,weight=1) #fila botones

    def styles(self):
        #Window style
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')
        self.estilo.configure(self, background='#1d2d44',
                              foreground='white',
                              fieldbackground='black'
                              )
        # conf Buttons
        self.estilo.configure('TButton', background='#005f73')  # Cambiar el contraste de colores del boton
        self.estilo.map('TButton',
                        background=[('active', '#0a9396')])  # Para contrastes al momento de posicionarse en el boton
        # Conf titulo
        etiqueta = ttk.Label(self, text='ZONA FIT GYM', font=('Time New Roman', 25))
        etiqueta.grid(row=0, column=0, columnspan=2)  # para centrar con la funcion columnspan

        # Conf_register
        self.estilo.map('Treeview',
                        background=[('selected',  # sentencia al seleccionar algun registro
                                     '#3a86ff'  # Cambia al color que queremos
                                     )])#Conf_table_treeview
        self.estilo.theme_use('clam')
        self.estilo.configure('Treeview', background='black',
                              foreground='white',
                              fieldbackground='black',
                              rowheight=30)

    def show_form(self):
        self.frame=ttk.Frame(self)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=3)
        # etiqueta titulo
        etiqueta = ttk.Label(self.frame, text='Formulario', font=('Arial', 20))
        etiqueta.grid(row=0, column=0, columnspan=2, sticky=tk.N)  # para centrar con la funcion columnspan
        # Usuario etiqueta
        nombre_etiqueta = ttk.Label(self.frame, text='Nombre: ', font=20)
        nombre_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=15)
        # Caja texto usuario
        self.box_name = ttk.Entry(self.frame)
        self.box_name.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)
        #Etiqueta_Apellido
        etiqueta_apellido=ttk.Label(self.frame,text='Apellido: ', font=20)
        etiqueta_apellido.grid(row=3,column=0, sticky=tk.NW, padx=5, pady=40)
        #Cajatexto_apellido
        self.box_apellido=ttk.Entry(self.frame)
        self.box_apellido.grid(row=3, column=1, sticky=tk.E, padx=5,pady=5)
        #Etiqueta_membresia
        etiqueta_mem=ttk.Label(self.frame, text='Membresia: ', font=20)
        etiqueta_mem.grid(row=5,column=0,sticky=tk.SW, padx=5, pady=5)
        #box_membresia
        self.box_mem=ttk.Entry(self.frame)
        self.box_mem.grid(row=5,column=1, sticky=tk.E, padx=5,pady=5)
        #Publicar frame
        self.frame.grid(row=1,column=0, sticky=tk.NW, padx=30, pady=20)  #PUBLICAR FRAME SINO NO APARECE

    def show_table(self):
        columnas= ('Id','Nombre', 'Apellido', 'Membresia')
        self.tabla=ttk.Treeview(self,columns=columnas,
                                show="headings")
        self.tabla.heading('Id',text='Id',anchor=tk.CENTER)
        self.tabla.heading('Nombre',text='Nombre')
        self.tabla.heading('Apellido',text='Apellido')
        self.tabla.heading('Membresia',text='Membresia')
        #Colum_format - Ind table
        self.tabla.column('Id', width=80)  # Son pixeles asi que son pequeñas
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Apellido', width=120)
        self.tabla.column('Membresia', width=120)
        # #Test_date
        # datos = ((1, 'Aldo','Dalanir', 24), (2, 'Daniela','Martinez', 24)) # Tupla de valores
        # for persona in datos:
        #     self.tabla.insert(parent='',index=tk.END,values=persona)
        # CREAR UN scrollbar(DEZLIZAR) -- BARRA DE DEZPLAZAMINTO
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=self.scrollbar.set)  # para sincrozinar sobre el eje la visualizacion de los registros de la tabla
        self.scrollbar.grid(row=1, column=1, sticky=tk.NE, padx=20, ipady=145, pady=20)
        #Public table
        self.tabla.grid(row=1,column=1, sticky=tk.NW,pady=20,ipadx=30)

    def show_buttons(self):#Conf_table_treeview
        # Boton Guardar
        self.boton1 = ttk.Button(self, text='Guardar')
        self.boton1.grid(row=2,column=0, sticky=tk.N, padx=50, ipadx=5, ipady=5)
        #Boton Eliminar
        self.boton2= ttk.Button(self, text='Eliminar')
        self.boton2.grid(row=2, column=0, columnspan=2, sticky=tk.N, ipadx=5,ipady=5)
        #Boton Limpiar
        self.boton3=ttk.Button(self, text='Limpiar')
        self.boton3.grid(row=2, column=1, sticky=tk.NE, padx=120, ipadx=5,ipady=5)

    def db_date_in_table(self):
        # Limpiar tabla
        self.tabla.delete(*self.tabla.get_children()) #Metodo que cuando se llama se limpia la tabla
        cliente=Cliente_DAO.seleccionar()
        for cliente in cliente:
            self.tabla.insert(parent='', index=tk.END, values=cliente)

    def clean_boxes(self, event=None):
        self.box_name.delete(0,tk.END)#Se encarga de eliminar todos los caracteres de la caja de texto
        self.box_apellido.delete(0, tk.END)
        self.box_mem.delete(0,tk.END)

    def validar_campos(self):
        nombre=self.box_name.get().strip()
        apellido=self.box_apellido.get().strip()
        mem=self.box_mem.get().strip()
        if not nombre or not apellido or not mem:  # Verificar que los campoc esten lelnos
            showerror(title='ZonaFit', message='LLena todos los campos para agregar un nuevo cliente!!!')
            return
        if not nombre.isalpha() or not apellido.isalpha():
            showerror(title='ZonaFit', message='Recuerda que los valores de "Nombre" y "Apellido" deben ser alfabéticos"')
            return
        if not mem.isdigit():
            showerror(title='ZonaFit', message='Recuerda que la membresia debe ser numerica')
            return
        return True

    def llenar_boxes(self, persona):
        nombre=self.persona[1]
        apellido=self.persona[2]
        mem=self.persona[3]
        # cargar las cajas
        self.box_name.insert(0, nombre)
        self.box_apellido.insert(0, apellido)
        self.box_mem.insert(0, mem)

    def clean_all(self, event=None):
        self.clean_boxes()
        self.db_date_in_table()

#------------------Eventos CRUD ----------------
    def insertar_datos(self, event=None):
        try:
            name = self.box_name.get()
            apellido = self.box_apellido.get()
            membresia = self.box_mem.get()
            if not self.selection_person():#VALIDAR SI ESTA VACIO O NO
                if self.validar_campos():  # Va a entrar si se tiene un nombre seleccionado
                    cliente = Cliente(nombre=name, apellido=apellido, membresia=membresia)
                    self.zona_fit.insertar(cliente)
                    showinfo(title='ZonaFit', message=f'Usuario con los datos:\n'
                                                      f'Nombre: {name}\n'
                                                      f'Apellido: {apellido}\n'
                                                      f'Membresia: {membresia}\n'
                                                      f'Ingresado correctamnete!!!')
            else:#SI seleccioinamos uno
                id=self.selection_person()[0]
                if self.validar_campos():  # Va a entrar si se tiene un nombre seleccionado
                    cliente=Cliente(id=id, nombre=name, apellido=apellido,membresia=membresia) #id, nombre, apellido, membresia
                    self.zona_fit.actualizar(cliente)
                    showinfo(title='ZonaFit', message=f'Cliente con ID:{id} - Actualizado...')
            self.db_date_in_table()  # PARA QUE APAREZCAN LOS NUEVOS DATOS UPDATE TABLE
        except Exception as error:
            showerror(title='ZonaFit', message=f'A ocurrido un error del tipo:'
                                               f'{error}')

    def selection_person(self, event=None):
        seleccion = self.tabla.selection() #Seleccion actual
        if not seleccion: #Si no esta seleccionado nada
            return None
        elemento_selecionado=self.tabla.selection()[0]#Seleccionar solo el primero elento de la tabla
        self.elemento=self.tabla.item(elemento_selecionado)
        self.persona=self.elemento['values']
        #Limpiamos el formulario
        self.clean_boxes()
        self.llenar_boxes(self.persona)
        return self.persona

    def eliminar_datos(self, event=None): #Usuario ya existentes
        try:
            persona=self.selection_person() #Verificamos quie no esta vacio
            if not persona: #Verificar que esta vacio
                showerror(title='ZonaFit', message='Selecciona un elemento de la tabla y presiona el boton eliminar')
                return  #Parar todo
            #Separar esas madres
            cliente_eliminado=Cliente(persona[0])
            self.zona_fit.eliminar(cliente_eliminado)
            showinfo(title='ZonaFit',message=f'Se eliminado correctamente al cliente:\n'
                                             f'ID: {persona[0]}\n'
                                             f'Nombre: {persona[1]}\n'
                                             f'Apellido: {persona[2]}\n'
                                             f'Membresia: {persona[3]}')
            self.clean_boxes()
            self.db_date_in_table() #Actualizar tabla
        except Exception as error:
            showerror(title='ZonaFit', message=f'A ocurrido un error del tipo:'
                                               f'{error}')

    def Events(self):
        #RECORDAR PASAR SIN PARENTESIS AQUI YA QUE ESTAS SE EJECUTAN DE INMEDIATO
        #Buttons
        self.boton1.bind('<Return>', self.insertar_datos) #Cuando damos enter (Tecla)
        self.boton1.bind('<Button-1>', self.insertar_datos) #Cuando damos click izquierdo con mouse
        self.boton2.bind('<Return>', self.eliminar_datos) #Al precinar Enter
        self.boton2.bind('<Button-1>',self.eliminar_datos) #Al precionar click izquierdo
        self.tabla.bind('<<TreeviewSelect>>', self.selection_person) #Al seleccionar
        self.boton3.bind('<Return>', self.clean_all) #Al oresuonar la tecla enter
        self.boton3.bind('<Button-1>', self.clean_all)#LA precionar con el click izquierdo con el raton

if __name__ =='__main__':#Constructor de la clase padre que es Tk
    app=App()
    app.mainloop()