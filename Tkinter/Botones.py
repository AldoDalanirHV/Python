import tkinter as tk #Para crear ventana
from tkinter import ttk  #Mejoras vosuales mejor que tk

#CREAR VENTANA
#Creamos un objeto de tipo ventana
ventana = tk.Tk()
ventana.geometry('600x400') #Pixeles (largp<-> , ancho ^I)
ventana.title('Kraken UX')
# #evitar redimencionar la ventana un tamaño fijo no modificable
# ventana.resizable(0,0)
#Color de la ventana.configure
ventana.configure(background='#1d2d44') #Buscar mas colores en web "htmlcolorcodes"

'''---------------------Botones--------------------'''
def saludar(nombre):
    print(f'Hola {nombre} te amo...')

#boton1=ttk.Button(ventana,text='enviar',command=saludar)  #(padre, texto, accion(no se usan(), ya que primero se debe presionar el boton))  IMPORTANTE!!!!!!
#SI DESEAMOS METER PARAMETROS ENTONCES DEBEMOS USAR LA FUNCION COMO UNA FUNCION LAMBDA
boton1=ttk.Button(ventana,text='enviar',command=lambda:saludar('Daniela'))

#Publivcar el boton
boton1.pack(pady=20)#margen de 20 pixeles

#Hacemos visible la ventana con mainloop
ventana.mainloop()