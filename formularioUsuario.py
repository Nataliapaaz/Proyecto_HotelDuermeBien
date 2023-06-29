from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

ventana.title('Formulario de usuario')

encabezado = Label(ventana, text='Formulario de Usuario')
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

#Funcion para recuperar el RUT
def getRut():
    resultadoRut.set(RUT.get())

RUT = StringVar()
resultadoRut = StringVar()
#campo de texto (RUT)
campoTexto = Entry(ventana, textvariable=RUT)
campoTexto.grid(row=1, column=1, padx=5, pady=5)

#probando si me recupera el rut
Label(ventana, text='RUT recuperado: ').grid(row=1, column=2, padx=5, pady=5)
Label(ventana, textvariable=resultadoRut).grid(row=1, column=3, padx=5, pady=5)
Button(ventana, text='Mostrar RUT', command=getRut).grid(row=1, column=4, padx=5, pady=5)

#label para el campo de texto (nombre)
label = Label(ventana, text='Nombre')
label.grid(row=2, column=0, padx=5, pady=5)

#Funcion para recuperar el nombre
def getNombre():
    resultadoNombre.set(nombre.get())

nombre = StringVar()
resultadoNombre = StringVar()
#campo de texto (nombre)
campoTexto = Entry(ventana, textvariable=nombre)
campoTexto.grid(row=2, column=1, padx=5, pady=5)

#probando si me recupera el nombre
Label(ventana, text='Nombre recuperado: ').grid(row=2, column=2, padx=5, pady=5)
Label(ventana, textvariable=resultadoNombre).grid(row=2, column=3, padx=5, pady=5)
Button(ventana, text='Mostrar nombre', command=getNombre).grid(row=2, column=4, padx=5, pady=5)

#label para el campo de texto (usuario)
label = Label(ventana, text='Usuario')
label.grid(row=3, column=0, padx=5, pady=5)

#Funcion para recuperar el Usuario
def getUsuario():
    resultadoUsuario.set(usuario.get())

usuario = StringVar()
resultadoUsuario = StringVar()

#campo de texto (usuario)
campoTexto = Entry(ventana, textovariable=usuario)
campoTexto.grid(row=3, column=1, padx=5, pady=5)

#label para el campo de texto (contraseña)
label = Label(ventana, text='Contraseña')
label.grid(row=4, column=0, padx=5, pady=5)

#Funcion para recuperar la contraseña
def getContrasena():
    resultadoContrasena.set(contrasena.get())

contrasena = StringVar()
resultadoContrasena = StringVar()

#campo de texto (contraseña)
campoTexto = Entry(ventana, textovariable=contrasena)
campoTexto.grid(row=4, column=1, padx=5, pady=5)

#label para el campo de texto (edad)
label = Label(ventana, text='Edad')
label.grid(row=5, column=0, padx=5, pady=5)

#Funcion para recuperar la edad
def getEdad():
    resultadoEdad.set(edad.get())

edad = StringVar()
resultadoEdad = StringVar()

#campo de texto (edad)
campoTexto = Entry(ventana, textovariable=edad)
campoTexto.grid(row=5, column=1, padx=5, pady=5)

boton = Button(ventana, text='Enviar')
boton.grid(row=6, column=1)
boton.config(padx=10, pady=10)

boton = Button(ventana, text='Ver datos')
boton.grid(row=7, column=1)
boton.config(padx=10, pady=10)

ventana.mainloop()