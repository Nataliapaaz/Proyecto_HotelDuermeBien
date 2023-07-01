from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry('500x500')

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


# ---- U S U A R I O -----
#label para el campo de texto (usuario)
label = Label(ventana, text='Usuario')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (usuario)
campoUsuario = Entry(ventana)
campoUsuario.grid(row=3, column=1, padx=5, pady=5)

# ---- C O N T R A S E Ñ A -----
#label para el campo de texto (contraseña)
label = Label(ventana, text='Contraseña')
label.grid(row=4, column=0, padx=5, pady=5)

#campo de texto (contraseña)
campoContrasena = Entry(ventana)
campoContrasena.grid(row=4, column=1, padx=5, pady=5)

# ---- E D A D -----
#label para el campo de texto (edad)
label = Label(ventana, text='Edad')
label.grid(row=5, column=0, padx=5, pady=5)

#campo de texto (edad)
campoEdad = Entry(ventana)
campoEdad.grid(row=5, column=1, padx=5, pady=5)

#funcion para obtener los datos del usuario
def obtenerDatosUsuario():
    datosUsuario = []
    datosUsuario.append(campoRut.get())
    datosUsuario.append(campoNombre.get())
    datosUsuario.append(campoUsuario.get())
    datosUsuario.append(campoContrasena.get())
    datosUsuario.append(campoEdad.get())
    label = Label(ventana, text=datosUsuario)
    label.grid(row=8, column=1, padx=5, pady=5)

#Este boton deberia poder mandar los datos del usuario a la base de datos
boton = Button(ventana, text='Enviar')
boton.grid(row=6, column=1)
boton.config(padx=10, pady=10)

#Boton para mostrar todos los datos que se ingresaron
boton = Button(ventana, text='Ver datos', command=obtenerDatosUsuario)
boton.grid(row=7, column=1)
boton.config(padx=10, pady=10)

#Esto hace que se ejecute la ventana
ventana.mainloop()