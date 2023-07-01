from tkinter import *
import os.path

class Ventana:
    def __init__(self):
        self.titulo = 'Hotel Duerme Bien App'
        self.icon = './images/logo.ico'
        self.size = '750x550'
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
            rutaIcono = os.path.abspath('./Tkinter/images/logo.ico')
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
        texto.pack(side=TOP)

    def addTextoSecundario(self, textoVisible):
        texto = Label(self.ventana, text=textoVisible )
        texto.config(
            fg='black',
            bg='white',
            font=('Century Gothic', 14),
            width=100,
            height=10
            )
        texto.pack(anchor=W)

    def addTextoPie(self, textoPie):
        marco = Frame(self.ventana, width=250, height=50)
        marco.config(bg='lightblue')
        marco.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)
        marco.pack_propagate(False)

        textoPie = Label(marco, text=textoPie)
        textoPie.config(
            bg='lightblue',
            font=('Century Gothic', 11),
            height=10,
            width=30,
            anchor=CENTER)
        textoPie.pack()

    def mostrar(self):
        self.ventana.mainloop()


#Creacion del objeto (ventana)

ventana = Ventana()
ventana.cargar()
ventana.addTexto('Bienvenido a Duerme Bien App')
ventana.addTextoSecundario('Por favor blablabla')
ventana.addTextoPie('Todos los derechos reservados')
ventana.mostrar()