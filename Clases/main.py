from habitacion import Habitacion
from usuario import Usuario
from reserva import Reserva
from tipohabitacion import TipoHabitacion
from tipousuario import TipoUsuario
from huesped import Huesped
from DAO import DAO


def validarNumero(numero):
    while True:
        try:
            valor = int(input(f'Ingrese {numero}: '))
            break
        except ValueError:
            print('Debe ingresar un número válido.')
    return valor


def registrarUsuario():
    dao = DAO()
    nombre = input('Ingrese nombre y apellido del usuario: ')
    usuario = input('Ingrese nombre de usuario: ')
    password = input('Ingrese su password: ')
    rut_duplicado = True
    while rut_duplicado:
        rut = input('Ingrese rut del usuario: ')
        # Validación de RUT duplicado
        if dao.existeRutUsuario(rut):
            print('Error: El RUT ingresado ya existe. Intente nuevamente.')
        else:
            rut_duplicado = False
    edad = validarNumero('la edad del usuario: ')
    datos = dao.obtenerTipos()
    print(datos)
    tipoUsuario = validarNumero("Ingrese numero correspondiente al tipo de usuario: ")
    #Validacion tipo de usuario valido
    tipoUsuarioValido = False
    for i in datos:
        if tipoUsuario == i[0]:
            tipoUsuario = i[0]
            tipoUsuarioValido = True
            break
    if tipoUsuarioValido:
        usuario = Usuario(rut, nombre, usuario, password, edad, tipoUsuario)
        dao = DAO()
        dao.registrarUsuario(usuario)
        print("Usuario ingresado correctamente")
    else:
        print("Error: El tipo de usuario ingresado no es válido.") 


def registrarTipoUsuario():
    dao = DAO()
    nombreTipoUsuario = input('Ingrese si es Encargado o Administrador: ').lower()
    # Validación de nombre de tipo de usuario repetido
    if nombreTipoUsuario == "encargado" or nombreTipoUsuario == "administrador":       
        # Validación de nombre de tipo de usuario duplicado
        if dao.existeTipoUsuario(nombreTipoUsuario):
            print('Error: El tipo de usuario ingresado ya existe. No se puede registrar.')
        else:
            tipoUsuario = TipoUsuario(nombreTipoUsuario)
            dao.registrarTipoUsuario(tipoUsuario)
            print("Tipo de usuario registrado correctamente")
    else:
        print("Tipo de usuario inválido")


def registrarHabitacion():
    dao = DAO()
    datosReserva = dao.obtenerIdReserva()
    datosTipoHabitacion = dao.obtenerIdTipoHabitacion()
    datosHuesped = dao.obtenerIdHuesped()
    #validacion numero de habitacion repetido
    while True:
        numero = input('Ingrese el número de la habitación: ')
        if dao.existeNumeroHabitacion(numero):
            print('Error: El número de habitación ingresado ya existe. Intente nuevamente.')
        else:
            break
    orientacion = input('Ingrese la orientación de la habitación: ')
    pregunta = input('La habitacion esta ocupada o disponible?: ').lower()
    ocupacion = "ocupada" if pregunta =="ocupada" else " disponible"
    respuesta = input("¿El cliente es encargado? (SI o NO): ").lower()
    idEncargado = "si" if respuesta == "si" else "no"
    #Validacion id de reserva existente
    while True:
        print(datosReserva)
        idReserva = validarNumero('el ID de la reserva asociada: ')
        for i in datosReserva:
            if idReserva == i[0]:
                idReserva = i[0]
                break
        else:
            print("El ID de reserva ingresado no existe. Intente nuevamente.")
            continue
        break
        #validacion id de habitacion existente
    while True:
        print(datosTipoHabitacion)
        idHabitacion = validarNumero('el ID de la habitación asociada: ')
        for x in datosTipoHabitacion:
            if idHabitacion == x[0]:
                idHabitacion = x[0]
                break
        else:
            print("El ID de habitación ingresado no existe. Intente nuevamente.")
            continue
        break
        #validacion huesped existente
    while True:
        print(datosHuesped)
        idHuesped = validarNumero('el ID del huésped asociado: ')
        for z in datosHuesped:
            if idHuesped == z[0]:
                idHuesped = z[0]
                break
        else:
            print("El ID del huésped ingresado no existe. Intente nuevamente.")
            continue
        break

    habitacion = Habitacion(numero, orientacion, ocupacion, idEncargado, idReserva, idHabitacion, idHuesped)
    dao.registrarHabitacion(habitacion)
    print('La habitación se registró correctamente.')
    
def registrarTipoHabitacion():
    numeroCamas = validarNumero('el número de camas de la habitación: ')
    numeroPasajeros = validarNumero('el número de pasajeros de la habitación: ')
    tipoHabitacion = TipoHabitacion(numeroCamas, numeroPasajeros,)
    dao = DAO()
    dao.registrarTipoHabitacion(tipoHabitacion)
    print('El tipo de habitación se registró correctamente:')


def registrarReserva():
    dao = DAO()
    datosHuesped = dao.obtenerIdHuesped()
    datosUsuario = dao.obtenerIdUsuario()
    #validacion numero de reserva repetido
    while True:
        numeroReserva = validarNumero('Ingrese el número de reserva: ')
        if dao.existeNumeroReserva(numeroReserva):
            print('Error: El número de Reserva ingresado ya existe. Intente nuevamente.')
        else:
            break
    fechaIngreso = input('Ingrese la fecha de ingreso (YYYY-MM-DD): ')
    fechaSalida = input('Ingrese la fecha de salida (YYYY-MM-DD): ')
    capacidad = validarNumero('la cantidad de huéspedes: ')
    print(datosUsuario)  
    while True:
        idUsuario = validarNumero("el ID del usuario: ")     
        # Validación de ID de usuario existente
        if any(idUsuario == i[0] for i in datosUsuario):
            break
        else:
            print("ID de usuario no válido. Intente nuevamente.") 
    print(datosHuesped)
    while True:
        idHuesped = validarNumero("el ID del huésped: ")     
        # Validación de ID de huésped existente
        if any(idHuesped == x[0] for x in datosHuesped):
            break
        else:
            print("ID de huésped no válido. Intente nuevamente.")
    reserva = Reserva(numeroReserva, fechaIngreso, fechaSalida, capacidad, idUsuario, idHuesped)
    dao.registrarReserva(reserva)
    print('La reserva se registró correctamente:')
    

def registrarHuesped():
    dao = DAO() 
    datosHabitacion = dao.obtenerIdHabitacion()
    rut_duplicado = True
    while rut_duplicado:
        rut = input('Ingrese rut del usuario: ')
        # Validación de RUT duplicado
        if dao.existeRutHuesped(rut):
            print('Error: El RUT ingresado ya existe. Intente nuevamente.')
        else:
            rut_duplicado = False   
    #validar nombre correcto
    nombre = input('Ingrese el nombre del huésped: ')
    edad = validarNumero('la edad del huésped: ')
    fechaIngreso = input('Ingrese la fecha de ingreso (YYYY-MM-DD): ')
    fechaSalida = input('Ingrese la fecha de salida (YYYY-MM-DD): ')
    print(datosHabitacion)
    codigoHabitacion = validarNumero('Ingrese el código de la habitación: ')
    #validacion codigo de habitacion
    for i in datosHabitacion:
        while True:
            if codigoHabitacion == i[0]:
                codigoHabitacion = i[0]
                huesped = Huesped(rut,nombre,edad,fechaIngreso,fechaSalida,codigoHabitacion,)
                dao.registrarHuesped(huesped)
                break
            break
    print('El huésped se registró correctamente:')



while True:
    print('---Menu---')
    print('1.- Registrar Usuario')
    print('2.- Registrar Habitacion')
    print('3.- Registrar Huesped')
    print('4.- Registrar Tipo de Habitacion')
    print('5.- Registrar Reserva')
    print('6.- Registrar Tipo de Usuario')
    print('9.- Salir')
    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        registrarUsuario()
    elif opcion == '2':
        registrarHabitacion()
    elif opcion == '3':
        registrarHuesped()
    elif opcion == '4':
        registrarTipoHabitacion()
    elif opcion == '5':
        registrarReserva()
    elif opcion =='6':
        registrarTipoUsuario()
    elif opcion == '9':
        print('Salir')
        break
    else:
        print('La opción ingresada no es válida.')
        print('Ingrese una nueva opción.')