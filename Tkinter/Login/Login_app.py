import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

#creacion de ventana
ventana=tk.Tk() #creamo la ventana
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')

#Gride de ventana
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)

#Crear estilos, crear objeto de tipo estilo
estilos=ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black') #foreground es para el color  de nuestro texto, y fieldbackground es el color de las cajas de texto

estilos.configure('TButton', background='#005f73') #Cambiar el contraste de colores del boton
estilos.map('TButton', background=[('active','#0a9396')]) #Para contrastes al momento de posicionarse en el boton

#Frame contenedor invisible
frame=ttk.Frame(ventana)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=3)

#etiqueta titulo
etiqueta=ttk.Label(frame, text='Login', font=('Arial',20))
etiqueta.grid(row=0,column=0, columnspan=2)#para centrar con la funcion columnspan

#Usuario
usuario_etiqueta=ttk.Label(frame,text='Usuario: ')
usuario_etiqueta.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)

#Caja texto usuario
usuario_caja_texto=ttk.Entry(frame)
usuario_caja_texto.grid(row=1,column=1,sticky=tk.E,padx=5,pady=5)

#password
password_etiqueta=ttk.Label(frame,text='Password: ')
password_etiqueta.grid(row=2,column=0,sticky=tk.W,padx=5,pady=5)

#Caja texto usuario
password_caja_texto=ttk.Entry(frame,show='*') #Para que no se vean las cosas
password_caja_texto.grid(row=2,column=1,sticky=tk.E,padx=5,pady=5)

#Boton
boton1=ttk.Button(frame,text='Ingresar')
boton1.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

def validar(event):
    usuario= usuario_caja_texto.get()
    password=password_caja_texto.get()
    #Si el usurario == root y la congtraseña es == admin son corrctos
    try:
        if usuario == 'root' and password == 'admin':
            #print(f'Usuario bienvenido ...')
            showinfo(title='Login',message='Usuario correcto')
        else:
            showerror(title='Login', message='Datos incorrectos')
    except Exception as error:
        print(f'A ocurrido un error del tipo -> {error} <-')

#NUEVO METODO PARA VER DESPUES DE QUE SE EJECUTE UNA ACCION(DESOUES DE LA CREACION DEL BOTON)
boton1.bind('<Return>', validar) #El metodo que se llama cuando se presiona enter
boton1.bind('<Button-1>', validar) #Al hacer click izquierdo en el mouse

#EVENTOS DE LOS BOTONES
'''Button-2   ->BOTON CENTRAL
   Button-3   ->BOTON DERECHO
   KeyPress   ->Presionar cualquier tecla
   FOCO:
   PUEDES ASOCIAR FUNCIONES QUE SE EJECUTEN CUANDO SE OBTENGA O PIERDA EK FOCO DE ENTRADA 
   MouseWheel:
   CUANDO DESPLAZAMIENTO DE LA RUEDAD DEL RATON'''



#Publicar frame
frame.grid()  #poner si pasa algo entre parentesis (row=0, column=0)

#publicar ventana
ventana.mainloop()