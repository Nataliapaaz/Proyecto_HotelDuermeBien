from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry('700x500')

ventana.title('Formulario de usuario')
ventana.iconbitmap('images/logo.ico')

encabezado = Label(ventana, text='Formulario de Usuario')
encabezado.config(
    fg='white',
    bg='darkblue',
    font=('Century Gothic', 18),
    padx=20,
    pady=20)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# ---- R U T -----
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

# ---- N O M B R E -----
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

# ---- U S U A R I O -----
#label para el campo de texto (usuario)
label = Label(ventana, text='Usuario')
label.grid(row=3, column=0, padx=5, pady=5)

#Funcion para recuperar el Usuario
def getUsuario():
    resultadoUsuario.set(usuario.get())

usuario = StringVar()
resultadoUsuario = StringVar()

#campo de texto (usuario)
campoTexto = Entry(ventana, textvariable=usuario)
campoTexto.grid(row=3, column=1, padx=5, pady=5)

# ---- C O N T R A S E Ñ A -----
#label para el campo de texto (contraseña)
label = Label(ventana, text='Contraseña')
label.grid(row=4, column=0, padx=5, pady=5)

#Funcion para recuperar la contraseña
def getContrasena():
    resultadoContrasena.set(contrasena.get())

contrasena = StringVar()
resultadoContrasena = StringVar()

#campo de texto (contraseña)
campoTexto = Entry(ventana, textvariable=contrasena)
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
campoTexto = Entry(ventana, textvariable=edad)
campoTexto.grid(row=5, column=1, padx=5, pady=5)

boton = Button(ventana, text='Enviar')
boton.grid(row=6, column=1)
boton.config(padx=10, pady=10)

resultado = StringVar()

#hacer que funcione mostrar los valores
def datos():
    resultado.set(RUT.get() + nombre.get() + usuario.get() + contrasena.get() + edad.get()) 
    mostrarDatos = Label(ventana, textvariable=resultado.set)
    mostrarDatos.grid(row=8, column=0, padx=5, pady=5)

def mostrarDatos():
    messagebox.showinfo(f'Datos de usuario:{resultado.get()}')

boton = Button(ventana, text='Ver datos', command=mostrarDatos)
boton.grid(row=7, column=1)
boton.config(padx=10, pady=10)


ventana.mainloop()