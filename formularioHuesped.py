from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

ventana.title('Formulario de huesped')

encabezado = Label(ventana, text='Formulario de Huesped')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para el campo de texto (RUT)
label = Label(ventana, text='RUT')
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto (RUT)
campoTexto = Entry(ventana)
campoTexto.grid(row=1, column=1, padx=5, pady=5)

#label para el campo de texto (nombre)
label = Label(ventana, text='Nombre')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (nombre)
campoTexto = Entry(ventana)
campoTexto.grid(row=2, column=1, padx=5, pady=5)

#label para el campo de texto (edad)
label = Label(ventana, text='Edad')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (edad)
campoTexto = Entry(ventana)
campoTexto.grid(row=3, column=1, padx=5, pady=5)

#label para el campo de texto (fecha de ingreso)
label = Label(ventana, text='Fecha de ingreso')
label.grid(row=4, column=0, padx=5, pady=5)

#campo de texto (fecha de ingreso)
campoTexto = Entry(ventana)
campoTexto.grid(row=4, column=1, padx=5, pady=5)

#label para el campo de texto (fecha de salida)
label = Label(ventana, text='Fecha de salida')
label.grid(row=5, column=0, padx=5, pady=5)

#campo de texto (fecha de salida)
campoTexto = Entry(ventana)
campoTexto.grid(row=5, column=1, padx=5, pady=5)

boton = Button(ventana, text='Enviar')
boton.grid(row=6, column=1)
boton.config(padx=10, pady=10)

ventana.mainloop()