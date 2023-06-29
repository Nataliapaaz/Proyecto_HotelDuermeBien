from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

ventana.title('Cargar habitaciones')

encabezado = Label(ventana, text='Cargar habitacion')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para el campo de texto (numero)
label = Label(ventana, text='Numero')
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto (numero)
campoTexto = Entry(ventana)
campoTexto.grid(row=1, column=1, padx=5, pady=5)

#label para el campo de texto (capacidad)
label = Label(ventana, text='Capacidad')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (capacidad)
campoTexto = Entry(ventana)
campoTexto.grid(row=2, column=1, padx=5, pady=5)

#label para el campo de texto (orientacion)
label = Label(ventana, text='Orientacion')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (orientacion)
campoTexto = Entry(ventana)
campoTexto.grid(row=3, column=1, padx=5, pady=5)

ventana.mainloop()