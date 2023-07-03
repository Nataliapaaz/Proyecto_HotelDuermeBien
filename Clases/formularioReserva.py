from tkinter import *
from reserva import Reserva
from DAO import DAO
from tkinter import messagebox

def formulario_reserva():
    ventana = Tk()
    ventana.geometry('600x800')

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
    numeroReserva = Entry(ventana)
    numeroReserva.grid(row=1, column=1, padx=5, pady=5)

    # ---- FECHA DE INGRESO -----
    #label para el campo de texto (Fecha de ingreso)
    label = Label(ventana, text='Fecha de ingreso (YYYY-MM-DD):')
    label.grid(row=2, column=0, padx=5, pady=5)

    #campo de texto (Fecha de ingreso)
    fechaIngreso  = Entry(ventana)
    fechaIngreso.grid(row=2, column=1, padx=5, pady=5)

    # ---- FECHA DE SALIDA -----
    #label para el campo de texto (Fecha de salida)
    label = Label(ventana, text='Fecha de salida (YYYY-MM-DD):')
    label.grid(row=3, column=0, padx=5, pady=5)

    #campo de texto (Fecha de salida)
    fechaSalida  = Entry(ventana)
    fechaSalida.grid(row=3, column=1, padx=5, pady=5)

    # ---- CAPACIDAD -----
    #label para el campo de texto (Capacidad)
    label = Label(ventana, text='Capacidad')
    label.grid(row=4, column=0, padx=5, pady=5)

    #campo de texto (Capacidad)
    capacidad = Entry(ventana)
    capacidad.grid(row=4, column=1, padx=5, pady=5)

    # ---- ID USUARIO -----
    #label para el campo de texto (huesped)
    label = Label(ventana, text='id usuario')
    label.grid(row=5, column=0, padx=5, pady=5)

    #campo de texto (huesped)
    idUsuario = Entry(ventana)
    idUsuario.grid(row=5, column=1, padx=5, pady=5)

    # ---- ID HUESPED -----
    #label para el campo de texto (usuario)
    label = Label(ventana, text='id huesped')
    label.grid(row=6, column=0, padx=5, pady=5)

    #campo de texto (usuario))
    idHuesped = Entry(ventana)
    idHuesped.grid(row=6, column=1, padx=5, pady=5)

    def validarNumero(numero):
        while True:
            try:
                valor = int(input(f'Ingrese {numero}: '))
                break
            except ValueError:
                print('Debe ingresar un número válido.')
        return valor

    def registrarReserva():
        dao = DAO()
        datosHuesped = dao.obtenerIdHuesped()
        datosUsuario = dao.obtenerIdUsuario()
        #validacion numero de reserva repetido

        print(datosUsuario)  
        while True:
            idUsuarioVal = int(idUsuario.get())   
        # Validación de ID de usuario existente
            if any(idUsuarioVal == i[0] for i in datosUsuario):
                break
            else:
                print("ID de usuario no válido. Intente nuevamente.") 
        print(datosHuesped)
        while True:
            idHuespedVal = int(idHuesped.get())  
        # Validación de ID de huésped existente
            if any(idHuespedVal == x[0] for x in datosHuesped):
                break
            else:
                print("ID de huésped no válido. Intente nuevamente.")
        reserva = Reserva(numeroReserva.get(), fechaIngreso.get(), fechaSalida.get(), capacidad.get(), idUsuarioVal, idHuespedVal)
        dao.registrarReserva(reserva)
        label = Label(ventana, text='Reserva ingresada correctamente')
        label.config(
            fg='white',
            bg='darkblue',
            font=('Century Gothic', 16),
            padx=20,
            pady=20)
        label.grid(row=14,  column=1, padx=5, pady=5)


    def mostrarTipoUsuario():
        dao= DAO()
        datosUsuario= dao.idUsuarios()         
        label = Label(ventana, text=datosUsuario)
        label.grid(row=12, column=0, padx=5, pady=5)

    def mostrarTipoHuesped():
        dao= DAO()         
        datosHuesped = dao.idHuespedes()
        label = Label(ventana, text=datosHuesped)
        label.grid(row=12, column=1, padx=5, pady=5)

    boton = Button(ventana, text='Mostrar id de usuario', command=mostrarTipoUsuario)
    boton.grid(row=11, column=0)
    boton.config(padx=10, pady=10)

    boton = Button(ventana, text='Mostrar id de huesped', command=mostrarTipoHuesped)
    boton.grid(row=11, column=1)
    boton.config(padx=10, pady=10)




    #funcion para crear una lista con los datos del usuario
    def obtenerDatosUsuario():
        datosUsuario = []
        datosUsuario.append(numeroReserva.get())
        datosUsuario.append(fechaIngreso.get())
        datosUsuario.append(fechaSalida.get())
        datosUsuario.append(idUsuario.get())
        label = Label(ventana, text=datosUsuario)
        label.grid(row=5, column=1, padx=5, pady=5)

    #Creacion de list box para mostrar los datos
    def crearListBox():
        listbox = Listbox(ventana)
        listbox.insert(0, numeroReserva.get(), fechaIngreso.get(), fechaSalida.get(), capacidad.get())
        listbox.grid(row=7, column=1, padx=5, pady=5)

    #Este boton deberia poder mandar los datos del usuario a la base de datos
    boton = Button(ventana, text='Enviar', command=registrarReserva)
    boton.grid(row=7, column=1)
    boton.config(padx=10, pady=10)

    #Boton para mostrar todos los datos que se ingresaron
    boton = Button(ventana, text='Ver datos', command=crearListBox)
    boton.grid(row=8, column=1)
    boton.config(padx=10, pady=10)

    #Esto hace que se ejecute la ventana
    ventana.mainloop()
