import tkinter as tk
from tkinter import ttk
#tkinter ya viene por defecto en python pero debes descargar tk aparte, asi que lo descargas desde terminal normal
#sudo pacman -S tk  (esto desde la terminal de python si es posible)

#CREAR VENTANA
#Creamos un objeto de tipo ventana
ventana = tk.Tk()
ventana.geometry('600x400') #Pixeles (largp<-> , ancho ^I)
ventana.title('Kraken UX')
# #evitar redimencionar la ventana un tamaño fijo no modificable
# ventana.resizable(0,0)
#Color de la ventana.configure
ventana.configure(background='#1d2d44') #Buscar mas colores en web "htmlcolorcodes"

'''-----------------------------------------ETIQUETAS----------------------------------------------------------------------------'''

#Etiqueta Texto que se va a visualizar en nuestra ventana de tkinter
#EXISTEN 3 FROMAS DE MODIFICAR TEXTO

#1 DESDE LE CONSTRUCTOR DE LA CLASE
etiqueta=ttk.Label(ventana,text='Putos') #Este componemte se debe publicar para visualizarlos   ----------> SE USA EL MODELO COMPONENTE ttk ya que es una mejora de tkinter

#2 CON EL METODO CONFIGURE
#Camabira el texto con el metodo configure
etiqueta.configure(text='Nos vemos gays')

#3 CON LLAVE TEXT
etiqueta['text']='Adios...'

etiqueta.pack(pady=20) #Para poder visualizar el contenido y moverlo con padx y pady

#Hacemos visible la ventana con mainloop
ventana.mainloop()