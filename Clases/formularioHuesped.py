from tkinter import *
from huesped import Huesped
from DAO import DAO
from tkinter import messagebox

def formulario_huesped():
    ventana = Tk()
    ventana.geometry('600x800')

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
    rut = Entry(ventana)
    rut.grid(row=1, column=1, padx=5, pady=5)

    # ---- N O M B R E -----
    #label para el campo de texto (nombre)
    label = Label(ventana, text='Nombre')
    label.grid(row=2, column=0, padx=5, pady=5)

    #campo de texto (nombre)
    nombre = Entry(ventana)
    nombre.grid(row=2, column=1, padx=5, pady=5)

    # ---- E D A D -----
    #label para el campo de texto (edad)
    label = Label(ventana, text='Edad')
    label.grid(row=3, column=0, padx=5, pady=5)

    #campo de texto (edad)
    edad = Entry(ventana)
    edad.grid(row=3, column=1, padx=5, pady=5)

    # ---- FECHA DE INGRESO -----
    #label para el campo de texto (fecha de ingreso)
    label = Label(ventana, text='Fecha de ingreso')
    label.grid(row=4, column=0, padx=5, pady=5)

    #campo de texto (fecha de ingreso)
    fechaIngreso = Entry(ventana)
    fechaIngreso.grid(row=4, column=1, padx=5, pady=5)

    # ---- FECHA DE SALIDA -----
    #label para el campo de texto (fecha de salida)
    label = Label(ventana, text='Fecha de salida')
    label.grid(row=5, column=0, padx=5, pady=5)

    #campo de texto (fecha de salida)
    fechaSalida = Entry(ventana)
    fechaSalida.grid(row=5, column=1, padx=5, pady=5)

    # ---- CODIGO HABITACION -----
    #label para el campo de texto (codigo habitacion)
    label = Label(ventana, text='Codigo habitacion')
    label.grid(row=6, column=0, padx=5, pady=5)

    #campo de texto (codigo habitacion)
    codigoHabitacion = Entry(ventana)
    codigoHabitacion.grid(row=6, column=1, padx=5, pady=5)

    def validarNumero(numero):
        while True:
            try:
                valor = int(input(f'Ingrese {numero}: '))
                break
            except ValueError:
                print('Debe ingresar un número válido.')
        return valor

    def registrarHuesped():
        dao = DAO() 
        datosHabitacion = dao.obtenerIdHabitacion()  
        #validar nombre correcto
        codigoHabitacionVal = int(codigoHabitacion.get())
        #validacion codigo de habitacion
        for i in datosHabitacion:
            while True:
                if codigoHabitacionVal == i[0]:
                    codigoHabitacionVal = i[0]
                    huesped = Huesped(rut.get(),nombre.get(),edad.get(),fechaIngreso.get(),fechaSalida.get(),codigoHabitacionVal,)
                    dao.registrarHuesped(huesped)
                    break
                break
        label = Label(ventana, text='Huesped ingresado correctamente')
        label.config(
            fg='white',
            bg='darkblue',
            font=('Century Gothic', 16),
            padx=20,
            pady=20)
        label.grid(row=9,  column=1, padx=5, pady=5)


    def mostrarHabitacion():
        dao= DAO()         
        datosHabitacion = dao.idHabitacion()
        label = Label(ventana, text=datosHabitacion)
        label.grid(row=12, column=1, padx=5, pady=5)

    boton = Button(ventana, text='Mostrar id de habitacion', command=mostrarHabitacion)
    boton.grid(row=11, column=1)
    boton.config(padx=10, pady=10)

#funcion para crear una lista con los datos del huesped
    def obtenerDatosHuesped():
        datosUsuario = []
        datosUsuario.append(rut.get())
        datosUsuario.append(nombre.get())
        datosUsuario.append(edad.get())
        datosUsuario.append(fechaIngreso.get())
        datosUsuario.append(fechaSalida.get())
        label = Label(ventana, text=datosUsuario)
        label.grid(row=8, column=1, padx=5, pady=5)

    #Creacion de list box para mostrar los datos
    def crearListBox():
        listbox = Listbox(ventana)
        listbox.insert(0, rut.get(), nombre.get(), edad.get(), fechaIngreso.get(), fechaSalida.get())
        listbox.grid(row=9, column=1, padx=5, pady=5)

    #Este boton ENVIAR, deberia poder mandar los datos del usuario a la base de datos
    boton = Button(ventana, text='Enviar', command = registrarHuesped)
    boton.grid(row=7, column=1)
    boton.config(padx=10, pady=10)

    #Boton para mostrar todos los datos que se ingresaron
    boton = Button(ventana, text='Ver datos', command=crearListBox)
    boton.grid(row=8, column=1)
    boton.config(padx=10, pady=10)

    ventana.mainloop()