from tkinter import *
import os.path

class Ventana:
    def __init__(self):
        self.titulo = 'Hotel Duerme Bien App'
        self.icon = './images/hotel-logo.ico'
        self.size = '750x450'
        self.resizable = False

    def cargar(self):
        ventana = Tk()
        #titulo
        ventana.title(self.titulo)
        #tamaño
        ventana.geometry(self.size)
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)
        rutaIcono = os.path.abspath(self.icon)
        if not os.path.isfile(rutaIcono):
            rutaIcono = os.path.abspath('./Tkinter/images/hotel-logo.ico')
        texto = Label(ventana, text=rutaIcono)
        texto.pack()
        #icono
        ventana.iconbitmap('hotel-logo.ico')
        ventana.mainloop()

#Creacion del objeto (ventana)

ventana = Ventana()
ventana.cargar()

