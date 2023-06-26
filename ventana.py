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
        self.ventana = ventana
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
        else:
            ventana.iconbitmap('hotel-logo.ico')

    def addTexto(self, textoVisible):
        texto = Label(self.ventana, text=textoVisible )
        texto.config(
            fg='white',
            bg='black',
            padx=750,
            pady=30,
            font=('Century Gothic', 20)
            )
        texto.pack()

    def addTextoSecundario(self, textoVisible):
        texto = Label(self.ventana, text=textoVisible )
        texto.config(
            fg='black',
            bg='white',
            font=('Century Gothic', 14),
            justify=RIGHT,
            anchor=W
            )
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()


#Creacion del objeto (ventana)

ventana = Ventana()
ventana.cargar()
ventana.addTexto('Bienvenido a Duerme Bien App')
ventana.addTextoSecundario('Por favor blablabla')
ventana.mostrar()