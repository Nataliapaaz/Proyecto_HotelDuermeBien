from tkinter import *
from DAO import DAO
from habitacion import Habitacion

def formulario_habitaciones():
    ventana = Tk()
    ventana.geometry('600x800')

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
    numero = Entry(ventana)
    numero.grid(row=1, column=1, padx=5, pady=5)

    # ---- ORIENTACIÓN -----
    #label para el campo de texto (orientacion)
    label = Label(ventana, text='Orientacion')
    label.grid(row=2, column=0, padx=5, pady=5)

    #campo de texto (orientacion)
    orientacion = Entry(ventana)
    orientacion.grid(row=2, column=1, padx=5, pady=5)

    # ---- OCUPACION -----
    #label para el campo de texto (capacidad)
    label = Label(ventana, text='Capacidad')
    label.grid(row=3, column=0, padx=5, pady=5)

    #campo de texto (capacidad)
    ocupacion = Entry(ventana)
    ocupacion.grid(row=3, column=1, padx=5, pady=5)

    label = Label(ventana, text='El huesped es encargado de habitacion? (si/no)')
    label.grid(row=4, column=0, padx=5, pady=5)
    encargadoHabitacion = Entry(ventana)
    encargadoHabitacion.grid(row=4, column=1, padx=5, pady=5)


    label = Label(ventana, text='Id de la reserva')
    label.grid(row=5, column=0, padx=5, pady=5)


    global idReserva
    idReserva = Entry(ventana)
    idReserva.grid(row=5, column=1, padx=5, pady=5)


    label = Label(ventana, text='Id de habitacion')
    label.grid(row=6, column=0, padx=5, pady=5)


    global idHabitacion
    idHabitacion = Entry(ventana)
    idHabitacion.grid(row=6, column=1, padx=5, pady=5)


    label = Label(ventana, text='Id de huesped')
    label.grid(row=7, column=0, padx=5, pady=5)


    global idHuesped
    idHuesped = Entry(ventana)
    idHuesped.grid(row=7, column=1, padx=5, pady=5)


    def validarNumero(numero):
        while True:
            try:
                valor = int(input(f'Ingrese {numero}: '))
                break
            except ValueError:
                print('Debe ingresar un número válido.')
        return valor


    #funcion para crear una lista con los datos la habitacion
    def obtenerDatosHabitacion():
        datosUsuario = []
        datosUsuario.append(numero.get())
        datosUsuario.append(ocupacion.get())
        datosUsuario.append(orientacion.get())
        label = Label(ventana, text=datosUsuario)
        label.grid(row=4, column=1, padx=5, pady=5)

    #Creacion de list box para mostrar los datos
    def crearListBox():
        listbox = Listbox(ventana)
        listbox.insert(0, numero.get(), ocupacion.get(), orientacion.get())
        listbox.grid(row=6, column=1, padx=5, pady=5)


    def registrarHabitacion():
        dao = DAO()
        datosReserva = dao.obtenerIdReserva()
        datosTipoHabitacion = dao.obtenerIdTipoHabitacion()
        datosHuesped = dao.obtenerIdHuesped()


        #Validacion id de reserva existente
        idReservaVal = int(idReserva.get())
        idHabitacionVal = int(idHabitacion.get())
        idHuespedVal = int(idHuesped.get())
        while True:
            print(datosReserva)
            for i in datosReserva:
                if idReservaVal == i[0]:
                    idReservaVal = i[0]
                    break
            else:
                print("El ID de reserva ingresado no existe. Intente nuevamente.")
                continue
            break
            #validacion id de habitacion existente
        while True:
            print(datosTipoHabitacion)

            for x in datosTipoHabitacion:
                if idHabitacionVal == x[0]:
                    idHabitacionVal = x[0]
                    break
            else:
                print("El ID de habitación ingresado no existe. Intente nuevamente.")
                continue
            break
            #validacion huesped existente
        while True:
            print(datosHuesped)

            for z in datosHuesped:
                if idHuespedVal == z[0]:
                    idHuespedVal = z[0]
                    break
            else:
                print("El ID del huésped ingresado no existe. Intente nuevamente.")
                continue
            break

        habitacion = Habitacion(numero.get(), orientacion.get(), ocupacion.get(), encargadoHabitacion.get(), idReservaVal, idHabitacionVal, idHuespedVal,)
        dao.registrarHabitacion(habitacion)
        label = Label(ventana, text='Habitacion ingresada correctamente')
        label.config(
            fg='white',
            bg='darkblue',
            font=('Century Gothic', 16),
            padx=20,
            pady=20)
        label.grid(row=14,  column=1, padx=5, pady=5)


    def mostrarTipoReserva():
        dao= DAO()
        datosReserva= dao.idReserva()         
        label = Label(ventana, text=datosReserva)
        label.grid(row=12, column=0, padx=5, pady=5)

    def mostrarTipoHuesped():
        dao= DAO()         
        datosHuesped = dao.idHuespedes()
        label = Label(ventana, text=datosHuesped)
        label.grid(row=12, column=2, padx=5, pady=5)

    def mostrarTipoHabitacion():
        dao = DAO()
        datosHabitacion = dao.idTipoHabitacion()
        label = Label(ventana, text = datosHabitacion)
        label.grid(row = 12, column=1,padx=5, pady=5)

    boton = Button(ventana, text='Mostrar id de reserva', command=mostrarTipoReserva)
    boton.grid(row=11, column=0)
    boton.config(padx=10, pady=10)

    boton = Button(ventana, text='Mostrar id del tipo de habitacion', command=mostrarTipoHabitacion)
    boton.grid(row=11, column=1)
    boton.config(padx=10, pady=10)

    boton = Button(ventana, text='Mostrar id de huesped', command=mostrarTipoHuesped)
    boton.grid(row=11, column=2)
    boton.config(padx=10, pady=10)

    #Este boton ENVIAR, deberia poder mandar los datos del usuario a la base de datos
    boton = Button(ventana, text='Enviar', command=registrarHabitacion)
    boton.grid(row=8, column=1)
    boton.config(padx=10, pady=10)

    #Boton para mostrar todos los datos que se ingresaron
    boton = Button(ventana, text='Ver datos', command=crearListBox)
    boton.grid(row=9, column=1)
    boton.config(padx=10, pady=10)

    ventana.mainloop()