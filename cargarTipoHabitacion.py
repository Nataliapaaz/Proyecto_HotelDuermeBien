from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

ventana.title('Cargar tipo de habitaciones')

encabezado = Label(ventana, text='Cargar tipo de habitacion')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para el campo de texto (numero de pasajeros)
label = Label(ventana, text='Numero de pasajeros permitido')
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto (numero de pasajeros)
campoTexto = Entry(ventana)
campoTexto.grid(row=1, column=1, padx=5, pady=5)

#label para el campo de texto (numero de camas)
label = Label(ventana, text='Numero de camas de la habitacion')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (numero de camas)
campoTexto = Entry(ventana)
campoTexto.grid(row=2, column=1, padx=5, pady=5)

boton = Button(ventana, text='Enviar')
boton.grid(row=3, column=1)
boton.config(padx=10, pady=10)

ventana.mainloop()