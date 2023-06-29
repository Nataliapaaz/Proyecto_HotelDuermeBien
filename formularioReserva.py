from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

ventana.title('Formulario de reserva')

encabezado = Label(ventana, text='Formulario de Reserva')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para el campo de texto (Numero de reserva)
label = Label(ventana, text='Numero de reserva')
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto (Numero de reserva)
campoTexto = Entry(ventana)
campoTexto.grid(row=1, column=1, padx=5, pady=5)

#label para el campo de texto (Fecha de ingreso)
label = Label(ventana, text='Fecha de ingreso')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (Fecha de ingreso)
campoTexto = Entry(ventana)
campoTexto.grid(row=2, column=1, padx=5, pady=5)

#label para el campo de texto (Fecha de salida)
label = Label(ventana, text='Fecha de salida')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (Fecha de salida)
campoTexto = Entry(ventana)
campoTexto.grid(row=3, column=1, padx=5, pady=5)

#label para el campo de texto (Capacidad)
label = Label(ventana, text='Capacidad')
label.grid(row=4, column=0, padx=5, pady=5)

#campo de texto (Capacidad)
campoTexto = Entry(ventana)
campoTexto.grid(row=4, column=1, padx=5, pady=5)


ventana.mainloop()