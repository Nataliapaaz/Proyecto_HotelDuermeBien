from tkinter import *

ventana = Tk()
ventana.geometry('400x600')

ventana.title('Cargar habitaciones')

encabezado = Label(ventana, text='Cargar habitacion')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# ---- N U M E R O -----
#label para el campo de texto (numero)
label = Label(ventana, text='Numero')
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto (numero)
campoNumero = Entry(ventana)
campoNumero.grid(row=1, column=1, padx=5, pady=5)

# ---- CAPACIDAD -----
#label para el campo de texto (capacidad)
label = Label(ventana, text='Capacidad')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (capacidad)
campoCapacidad = Entry(ventana)
campoCapacidad.grid(row=2, column=1, padx=5, pady=5)

# ---- ORIENTACIÓN -----
#label para el campo de texto (orientacion)
label = Label(ventana, text='Orientacion')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (orientacion)
campoOrientacion = Entry(ventana)
campoOrientacion.grid(row=3, column=1, padx=5, pady=5)

#funcion para crear una lista con los datos la habitacion
def obtenerDatosHabitacion():
    datosUsuario = []
    datosUsuario.append(campoNumero.get())
    datosUsuario.append(campoCapacidad.get())
    datosUsuario.append(campoOrientacion.get())
    label = Label(ventana, text=datosUsuario)
    label.grid(row=4, column=1, padx=5, pady=5)

#Creacion de list box para mostrar los datos
def crearListBox():
    listbox = Listbox(ventana)
    listbox.insert(0, campoNumero.get(), campoCapacidad.get(), campoOrientacion.get())
    listbox.grid(row=6, column=1, padx=5, pady=5)

#Este boton ENVIAR, deberia poder mandar los datos del usuario a la base de datos
boton = Button(ventana, text='Enviar')
boton.grid(row=4, column=1)
boton.config(padx=10, pady=10)

#Boton para mostrar todos los datos que se ingresaron
boton = Button(ventana, text='Ver datos', command=crearListBox)
boton.grid(row=5, column=1)
boton.config(padx=10, pady=10)

ventana.mainloop()