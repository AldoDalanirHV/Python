from readline import backend
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

#Crear ventana
ventana=tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de tablas')
ventana.configure(background='#1d2d44')

#Conf de grid
ventana.columnconfigure(0,weight=1) #Para centrarlas solo una columna
ventana.columnconfigure(1,weight=0)

#estilo
estilo=ttk.Style()
estilo.theme_use('clam')#prepaea el menejo del tema oscuro
estilo.configure('Treeview', background='black',
                 foreground='white',  #color de texto
                 fieldbackground='black', #color de fondo de la tabla
                 rowheight=30 #tamaño en pixeles de cada uno de los registros
                 )
#al seleccionar los registros
estilo.map('Treeview',
           background=[('selected', #sentencia al seleccionar algun registro
                                   '#3a86ff' #Cambia al color que queremos
                        )])

#----------------------------------CODIGO TABLA------------------------------
#definir las columnas
columnas= ('Id','Name', 'Age')
tabla=ttk.Treeview(ventana, columns=columnas, show='headings') #Paquete que crea un componente de tabla con la tupla de valores que queremos usar
#Headings es solo para mostrar los cabeceros no para un treeview(para sunregistros)

#Cabeceras de tabla
tabla.heading('Id',text='Id',anchor=tk.CENTER) #Me parece que pueden ser iguales
tabla.heading('Name',text='Name', anchor=tk.W) #Para hacer a la izquierda o donde sea
tabla.heading('Age',text='Age', anchor=tk.W)    #Primer columna no se dezpliega ya que ahi se muestar inf ma detalle de los registros ya que es un 'Treeview'

#Inf de tabla  -  fromato de columnas
tabla.column('Id', width=80) #Son pixeles asi que son pequeñas
tabla.column('Name', width=120)
tabla.column('Age',width=120)

#Cargar datos a la tabla
datos=((1,'Aldo',24),(2,'Daniela',24)) #Tupla de valores

#datos=((1,'Aldo',24),(2,'Daniela',24)) + ((1,'Aldo',24),(2,'Daniela',24)) + ((1,'Aldo',24),(2,'Daniela',24)) + ((1,'Aldo',24),(2,'Daniela',24)) +((1,'Aldo',24),(2,'Daniela',24)) +((1,'Aldo',24),(2,'Daniela',24))+((1,'Aldo',24),(2,'Daniela',24))+((1,'Aldo',24),(2,'Daniela',24))+((1,'Aldo',24),(2,'Daniela',24))+((1,'Aldo',24),(2,'Daniela',24))#Tupla de valores
#Tupla de valore

#iterar para insertar los valores
for persona in datos:
    tabla.insert(parent='',index=tk.END ,values=persona)

#CREAR UN scrollbar(DEZLIZAR) -- BARRA DE DEZPLAZAMINTO
scrollbar=ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set) #para sincrozinar sobre el eje la visualizacion de los registros de la tabla
scrollbar.grid(row=0, column=1, sticky=tk.NS)

#mostarr reg seleccionado
def mostrar_registro_seleccionado(event):
    print(f'metodo mostrar registro seleecionado')
    elemento_select=tabla.selection()[0] #Solo el primer registro seleccionado
    elemento=tabla.item(elemento_select) #item=elementp
    persona= elemento['values'] #Tupla de personas
    print(f'La inf de la persona seleccionada es: ID: {persona[0]} - NOMBRE:{persona[1]} - Membresia: {persona[2]}')
    showinfo(title='Persona seleccionada', message=f'Inf de la persona{persona}')

#asociar el evento select a la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_registro_seleccionado)

#Publicar tabla
tabla.grid(row=0,column=0,sticky=tk.NSEW)

ventana.mainloop()