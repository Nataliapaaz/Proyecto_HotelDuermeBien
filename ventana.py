from tkinter import *
import os.path

ventana = Tk()

#titulo
ventana.title('Hotel Duerme Bien App')

#tamaño
ventana.geometry('750x450')

rutaIcono = os.path.abspath('./images/hotel-logo.ico')

if not os.path.isfile(rutaIcono):
    rutaIcono = os.path.abspath('./Tkinter/images/hotel-logo.ico')

texto = Label(ventana, text=rutaIcono)
texto.pack()

#icono
ventana.iconbitmap('hotel-logo.ico')

ventana.mainloop()