from tkinter import *
from usuario import Usuario
from DAO import DAO
from tkinter import messagebox

ventana = Tk()
ventana.geometry('600x800')

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
rut = Entry(ventana)
rut.grid(row=1, column=1, padx=5, pady=5)


# ---- N O M B R E -----
#label para el campo de texto (nombre)
label = Label(ventana, text='Nombre')
label.grid(row=2, column=0, padx=5, pady=5)

#campo de texto (nombre)
nombre = Entry(ventana)
nombre.grid(row=2, column=1, padx=5, pady=5)

# ---- U S U A R I O -----
#label para el campo de texto (usuario)
label = Label(ventana, text='Usuario')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (usuario)
usuario = Entry(ventana)
usuario.grid(row=3, column=1, padx=5, pady=5)

# ---- C O N T R A S E Ñ A -----
#label para el campo de texto (contraseña)
label = Label(ventana, text='Contraseña')
label.grid(row=4, column=0, padx=5, pady=5)

#campo de texto (contraseña)
password = Entry(ventana)
password.grid(row=4, column=1, padx=5, pady=5)

# ---- E D A D -----
#label para el campo de texto (edad)
label = Label(ventana, text='Edad')
label.grid(row=5, column=0, padx=5, pady=5)

#campo de texto (edad)
edad = Entry(ventana)
edad.grid(row=5, column=1, padx=5, pady=5)

#label para el campo de texto (id tipo de usuario)
label = Label(ventana, text='Id tipo de usuario')
label.grid(row=6, column=0, padx=5, pady=5)

#campo de texto (contraseña)
global idTipoUsuario
idTipoUsuario = Entry(ventana)
idTipoUsuario.grid(row=6, column=1, padx=5, pady=5)


def validarNumero(numero):
    while True:
        try:
            valor = int(input(f'Ingrese {numero}: '))
            break
        except ValueError:
            messagebox.showinfo(message="La edad no es valida", title="Error")
    return valor

def registrarUsuario():
    dao = DAO()
    rut_duplicado = True
    edadValida = (int(edad.get()))
    while rut_duplicado:
        # Validación de RUT duplicado
        if dao.existeRutUsuario(rut.get()):
            print('Error: El RUT ingresado ya existe. Intente nuevamente.')
        else:
            rut_duplicado = False
    datos = dao.obtenerTipos()
    print(datos)
    #tipoUsuario = validarNumero("Ingrese numero correspondiente al tipo de usuario: ")
    #Validacion tipo de usuario valido
    tipoUsuarioValido = False
    tipoUsuario=int(idTipoUsuario.get())
    for i in datos:

        if tipoUsuario == i[0]:
            tipoUsuario = i[0]
            tipoUsuarioValido = True
            break
    if tipoUsuarioValido == True:
        global usuario
        usuario = Usuario(rut.get(), nombre.get(), usuario.get(), password.get(), edadValida, tipoUsuario,)
        dao = DAO()
        dao.registrarUsuario(usuario)
        label = Label(ventana, text='Usuario ingresado correctamente')
        label.config(
            fg='white',
            bg='darkblue',
            font=('Century Gothic', 16),
            padx=20,
            pady=20)
        label.grid(row=14,  column=1, padx=5, pady=5)
    else:
        print("Error: El tipo de usuario ingresado no es válido.") 


#funcion para crear una lista con los datos del usuario
def mostrarTipoUsuario():
    label = Label(ventana, text='Ingrese el numero 4 para Encargado')
    label.grid(row=12, column=1, padx=5, pady=5)
    label2 = Label(ventana, text='Ingrese el numero 5 para Administrador')
    label2.grid(row=13, column=1, padx=5, pady=5)

boton = Button(ventana, text='Mostrar tipos de usuario', command=mostrarTipoUsuario)
boton.grid(row=11, column=1)
boton.config(padx=10, pady=10)

def obtenerDatosUsuario():
    datosUsuario = []
    datosUsuario.append(rut.get())
    datosUsuario.append(nombre.get())
    datosUsuario.append(usuario.get())
    datosUsuario.append(password.get())
    datosUsuario.append(edad.get())
    label = Label(ventana, text=datosUsuario)
    label.grid(row=8, column=1, padx=5, pady=5)

#Creacion de list box para mostrar los datos
def crearListBox():
    listbox = Listbox(ventana)
    listbox.insert(0, rut.get(), nombre.get(), usuario.get(), password.get(), edad.get())
    listbox.grid(row=9, column=1, padx=5, pady=5)

#Este boton ENVIAR, deberia poder mandar los datos del usuario a la base de datos
boton = Button(ventana, text='Registrar usuario', command=registrarUsuario)
boton.grid(row=7, column=1)
boton.config(padx=10, pady=10)

# boton = Button(ventana, text='Ver datos', command=obtenerDatosUsuario)
# boton.grid(row=7, column=1)
# boton.config(padx=10, pady=10)

#Boton para mostrar todos los datos que se ingresaron
boton = Button(ventana, text='Ver datos', command=crearListBox)
boton.grid(row=8, column=1)
boton.config(padx=10, pady=10)

#Esto hace que se ejecute la ventana
ventana.mainloop()