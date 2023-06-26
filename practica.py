from tkinter import *

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

ventana.mainloop()