#Grid=rejilla ó cuadricula -> renglones y columnas para poder publicar nuestros renglones BASICAMENTE UNA MATRIZ
#Nueva forma de publicar elementos

import tkinter as tk #Para crear ventana
from tkinter import ttk  #Mejoras vosuales mejor que tk

# CODIGO BASICO PARA CREAR VENTANA
ventana = tk.Tk()
ventana.geometry('600x400') #Pixeles (largp<-> , ancho ^I)
ventana.title('Kraken UX')
ventana.configure(background='#1d2d44') #Buscar mas colores en web "htmlcolorcodes"

#Menejo de Grid
boton1=ttk.Button(ventana,text='boton1')
boton2=ttk.Button(ventana,text='boton2')
boton3=ttk.Button(ventana,text='boton3')

#Llamamos el boton de grid de forma mas facil
#Oublicados de manera horizintal. vertical
boton1.grid(row=0,column=0)
boton2.grid(row=1,column=1)
boton3.grid(row=2,column=2)


#Hacemos visible la ventana con mainloop
ventana.mainloop()