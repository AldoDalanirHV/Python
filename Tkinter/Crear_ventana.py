import tkinter as tk
#tkinter ya viene por defecto en python pero debes descargar tk aparte, asi que lo descargas desde terminal normal
#sudo pacman -S tk  (esto desde la terminal de python si es posible)

#Creamos un objeto de tipo ventana
ventana = tk.Tk()

#redimencionamos el tamaño de la ventana
ventana.geometry('600x400') #Pixeles (largp<-> , ancho ^I)
#modofcamos el titulo
ventana.title('Kraken UX')

#evitar redimencionar la ventana un tamaño fijo no modificable
ventana.resizable(0,0)

#Color de la ventana.configure
ventana.configure(background='#1d2d44') #Buscar mas colores en web "htmlcolorcodes"

#Hacemos visible la ventana con mainloop
ventana.mainloop()