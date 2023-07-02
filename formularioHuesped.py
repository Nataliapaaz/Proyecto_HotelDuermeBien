from tkinter import *

ventana = Tk()
ventana.geometry('400x600')

ventana.title('Formulario de huesped')

encabezado = Label(ventana, text='Formulario de Huesped')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)

# ---- R U T -----
#label para el campo de texto (RUT)
label = Label(ventana, text='RUT')
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto (RUT)
campoRut = Entry(ventana)
campoRut.grid(row=1, column=1, padx=5, pady=5)

# ---- N O M B R E -----
#label para el campo de texto (nombre)
label = Label(ventana, text='Nombre')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (nombre)
campoNombre = Entry(ventana)
campoNombre.grid(row=2, column=1, padx=5, pady=5)

# ---- E D A D -----
#label para el campo de texto (edad)
label = Label(ventana, text='Edad')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (edad)
campoEdad = Entry(ventana)
campoEdad.grid(row=3, column=1, padx=5, pady=5)

# ---- FECHA DE INGRESO -----
#label para el campo de texto (fecha de ingreso)
label = Label(ventana, text='Fecha de ingreso')
label.grid(row=4, column=0, padx=5, pady=5)

#campo de texto (fecha de ingreso)
campoIngreso = Entry(ventana)
campoIngreso.grid(row=4, column=1, padx=5, pady=5)

# ---- FECHA DE SALIDA -----
#label para el campo de texto (fecha de salida)
label = Label(ventana, text='Fecha de salida')
label.grid(row=5, column=0, padx=5, pady=5)

#campo de texto (fecha de salida)
campoSalida = Entry(ventana)
campoSalida.grid(row=5, column=1, padx=5, pady=5)

#funcion para crear una lista con los datos del huesped
def obtenerDatosHuesped():
    datosUsuario = []
    datosUsuario.append(campoRut.get())
    datosUsuario.append(campoNombre.get())
    datosUsuario.append(campoEdad.get())
    datosUsuario.append(campoIngreso.get())
    datosUsuario.append(campoSalida.get())
    label = Label(ventana, text=datosUsuario)
    label.grid(row=8, column=1, padx=5, pady=5)

#Creacion de list box para mostrar los datos
def crearListBox():
    listbox = Listbox(ventana)
    listbox.insert(0, campoRut.get(), campoNombre.get(), campoEdad.get(), campoIngreso.get(), campoSalida.get())
    listbox.grid(row=9, column=1, padx=5, pady=5)

#Este boton ENVIAR, deberia poder mandar los datos del usuario a la base de datos
boton = Button(ventana, text='Enviar')
boton.grid(row=6, column=1)
boton.config(padx=10, pady=10)

#Boton para mostrar todos los datos que se ingresaron
boton = Button(ventana, text='Ver datos', command=crearListBox)
boton.grid(row=7, column=1)
boton.config(padx=10, pady=10)

ventana.mainloop()