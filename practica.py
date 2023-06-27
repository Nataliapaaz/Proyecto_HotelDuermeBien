from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry('500x500')

texto = Label(ventana, text='Bienvenido a Duerme Bien app')
texto.config(
            fg='white',
            bg='black'
            )
texto.pack()

texto = Label(ventana, text='Por favor ingresa tu usuario y tu contraseña')
texto.pack()

imagen = Image.open('./Tkinter/images/1.png')
render = imageTk.PhotoImagen(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()