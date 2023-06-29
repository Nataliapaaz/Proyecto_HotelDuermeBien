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

marco = Frame(ventana, width=250, height=50)
marco.config(bg='lightblue')
marco.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)
marco.pack_propagate(False)

textoPie = Label(marco, text='todos los derechos reservados')
textoPie.config(
    bg='lightblue',
    font=('Century Gothic', 11))
textoPie.pack(side=BOTTOM, anchor=CENTER)

ventana.mainloop()