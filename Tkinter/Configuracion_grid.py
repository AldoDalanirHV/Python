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

#Configuracion de grid para ver como se comportan las columnas con el metyodo grid
ventana.columnconfigure(0,weight=1) #weight =Peso enytre mas peso + espacio ancho ocupa, e relacion a las otras que estamos publicando
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)

#Configuracion de filas
ventana.rowconfigure(0,weight=1) #weight =Peso enytre mas peso + espacio ancho ocupa, e relacion a las otras que estamos publicando
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)

#Publicacion horizontal, usando la funcion sticky pa moverla dentro de las celdas creadas, (N,S,E,W, Y MEZCLAR ENTRE ESTOS)
boton1.grid(row=0,column=0, padx=20,pady=20, ipadx=30, ipady=30) #pad -> añade pixeles para margenes
boton2.grid(row=0,column=1, sticky=tk.EW, ipadx=20, ipady=20) #ipad-> añae pixeles de manera internos
boton3.grid(row=0,column=2, sticky=tk.NW)

#Publicacion vertical
# boton1.grid(row=0,column=0)
# boton2.grid(row=1,column=0)
# boton3.grid(row=2,column=0)


#Publicacion de estos en diagonal
# boton1.grid(row=0,column=0)
# boton2.grid(row=1,column=1)
# boton3.grid(row=2,column=2)


#Hacemos visible la ventana con mainloop
ventana.mainloop()