import tkinter as tk #Para crear ventana
from tkinter import ttk  #Mejoras vosuales mejor que tk

# CODIGO BASICO PARA CREAR VENTANA
ventana = tk.Tk()
ventana.geometry('600x400') #Pixeles (largp<-> , ancho ^I)
ventana.title('Kraken UX')
ventana.configure(background='#1d2d44') #Buscar mas colores en web "htmlcolorcodes"


def mostrar():
    texto=caja_texto.get() #Aqui recuperamos lo qu ese haya escrito en la caja de texto
    print(f'Texto proporcionado: {texto}')
    etiqueta['text']=texto #Accedemos ocn la llave para cobre escribir el nombre de la etiqueta


#CREAR CAJA DE TEXTO  (Lugar en blanco para escrobibir)
caja_texto=ttk.Entry(ventana,font=('Arial',15))
caja_texto.pack(pady=20)

#Agregamos un boton
boton1=ttk.Button(ventana,text='enviar',command=mostrar)
boton1.pack(pady=20)


#Agregamos etiqueta
etiqueta=ttk.Label(ventana, text='valor inicial')
etiqueta.pack(pady=20)

#Hacemos visible la ventana con mainloop
ventana.mainloop()