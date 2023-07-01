from tkinter import *

ventana = Tk()
ventana.geometry('400x600')

ventana.title('Formulario de reserva')

encabezado = Label(ventana, text='Formulario de Reserva')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# ---- NUMERO DE RESERVA -----
#label para el campo de texto (Numero de reserva)
label = Label(ventana, text='Numero de reserva')
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto (Numero de reserva)
campoReserva = Entry(ventana)
campoReserva.grid(row=1, column=1, padx=5, pady=5)

# ---- FECHA DE INGRESO -----
#label para el campo de texto (Fecha de ingreso)
label = Label(ventana, text='Fecha de ingreso')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (Fecha de ingreso)
campoIngreso = Entry(ventana)
campoIngreso.grid(row=2, column=1, padx=5, pady=5)

# ---- FECHA DE SALIDA -----
#label para el campo de texto (Fecha de salida)
label = Label(ventana, text='Fecha de salida')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (Fecha de salida)
campoSalida = Entry(ventana)
campoSalida.grid(row=3, column=1, padx=5, pady=5)

# ---- CAPACIDAD -----
#label para el campo de texto (Capacidad)
label = Label(ventana, text='Capacidad')
label.grid(row=4, column=0, padx=5, pady=5)

#campo de texto (Capacidad)
campoCapacidad = Entry(ventana)
campoCapacidad.grid(row=4, column=1, padx=5, pady=5)

#funcion para crear una lista con los datos del usuario
def obtenerDatosUsuario():
    datosUsuario = []
    datosUsuario.append(campoReserva.get())
    datosUsuario.append(campoIngreso.get())
    datosUsuario.append(campoSalida.get())
    datosUsuario.append(campoCapacidad.get())
    label = Label(ventana, text=datosUsuario)
    label.grid(row=5, column=1, padx=5, pady=5)

#Creacion de list box para mostrar los datos
def crearListBox():
    listbox = Listbox(ventana)
    listbox.insert(0, campoReserva.get(), campoIngreso.get(), campoSalida.get(), campoCapacidad.get())
    listbox.grid(row=7, column=1, padx=5, pady=5)

#Este boton deberia poder mandar los datos del usuario a la base de datos
boton = Button(ventana, text='Enviar')
boton.grid(row=5, column=1)
boton.config(padx=10, pady=10)

#Boton para mostrar todos los datos que se ingresaron
boton = Button(ventana, text='Ver datos', command=crearListBox)
boton.grid(row=6, column=1)
boton.config(padx=10, pady=10)

#Esto hace que se ejecute la ventana
ventana.mainloop()