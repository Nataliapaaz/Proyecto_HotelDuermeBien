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

def obtenerTipoUsuario(idTipoUsuario):
    tiposUsuario = [
        TipoUsuario("1", "Administrador"),
        TipoUsuario("2", "Encargado"),
        TipoUsuario("3", "Invitado")
    ]

    for tipoUsuario in tiposUsuario:
        if tipoUsuario.getIdTipoUsuario() == idTipoUsuario:
            return tipoUsuario

    return None



def registrarUsuario():
    nombre = input('Ingrese nombre y apellido del usuario: ')
    usuario = input('Ingrese nombre de usuario: ')
    password = input('Ingrese su password: ')
    rut = input('Ingrese rut del usuario: ')
    edad = validarNumero('la edad del usuario: ')
    #tipoUsuario = obtenerTipoUsuario(idTipoUsuario)

    #if tipoUsuario is None:
        #print('El tipo de usuario ingresado no existe.')
        #return


    dao =DAO()
    obtenerId =dao.obtenerTipos()
    

    print(type(obtenerId))
    idTipoUsuario = input("Ingrese si es encargado o admnistrador: ").lower()

    for i in obtenerId:
        if i[0]== "encargado":
            idTipoUsuario = i[0]
            usuario = Usuario(rut,nombre, usuario, password, edad,idTipoUsuario )
            dao = DAO()
            dao.registrarUsuario(usuario)
            break
        elif i[1]== "ädministrador":
            idTipoUsuario = i[1]
            usuario = Usuario(rut,nombre, usuario, password, edad,idTipoUsuario )
            dao = DAO()
            dao.registrarUsuario(usuario)
            break
        else:
            print("El id no fue encontrado, intente nuevamente: ")

    print('El usuario se registró correctamente:')



def registrarTipoUsuario(lista_tipos_usuario):
    
    while True:    
        nombreTipoUsuario = input('Ingrese si es Encargado o Administrador: ').lower()
    
# Validación de nombre de tipo de usuario repetido
        if nombreTipoUsuario == "encargado":
            idTipoUsuario = 1
            tipoUsuario = TipoUsuario(idTipoUsuario,nombreTipoUsuario )
            dao = DAO()
            dao.registrarTipoUsuario(tipoUsuario)
            break
        elif nombreTipoUsuario == "administrador":
            idTipoUsuario = 2
            tipoUsuario = TipoUsuario(idTipoUsuario,nombreTipoUsuario)
            dao = DAO()
            dao.registrarTipoUsuario(tipoUsuario)
            break
        else:
            print("Tipo de usuario invalido, intente nuevamente")
            

def registrarHabitacion(lista_habitaciones):
    codigoHabitacion = input('Ingrese el código de la habitación: ')
    numero = input('Ingrese el número de la habitación: ')

# Validación de número de habitación repetido
    for habitacion in lista_habitaciones:
        if habitacion.getNumero() == numero:
            print('Error: El número de habitación ya existe.')
            return

    orientacion = input('Ingrese la orientación de la habitación: ')
    ocupacion = input('Ingrese la ocupación de la habitación: ')
    idReserva = input('Ingrese el ID de la reserva asociada: ')
    idHabitacion = input('Ingrese el ID de la habitación asociada: ')
    idHuesped = input('Ingrese el ID del huésped asociado: ')

    huesped = Huesped(idHuesped)
    tipoHabitacion = TipoHabitacion(idHabitacion)
    reserva = Reserva(idReserva)

# Validación de rut de huespde asignación a más de una habitación
    for habitacion in lista_habitaciones:
        if habitacion.getHuesped().getRut() == huesped.getRut():
            print('Error: El pasajero ya está asignado a otra habitación.')
            return

    habitacion = Habitacion(numero, orientacion, ocupacion, reserva, tipoHabitacion, huesped)

    dao = DAO()
    dao.registrarHabitacion(habitacion)  # Lógica para almacenar la habitación en la base de datos o en la lista de habitaciones

    print('La habitación se registró correctamente:')
    print(habitacion)
    print('Huésped:')
    print(huesped)
    print('Tipo de Habitación:')
    print(tipoHabitacion)
    print('Reserva:')
    print(reserva)

    
def registrarTipoHabitacion(lista_tipos_habitacion):
    numeroCamas = validarNumero('el número de camas de la habitación: ')
    numeroPasajeros = validarNumero('el número de pasajeros de la habitación: ')

    # Validación de ID de habitación repetido
    
    tipoHabitacion = TipoHabitacion(numeroCamas, numeroPasajeros,)

    dao = DAO()
    dao.registrarTipoHabitacion(tipoHabitacion)


    lista_tipos_habitacion.append(tipoHabitacion)



    print('El tipo de habitación se registró correctamente:')
    print(tipoHabitacion)


def registrarReserva():
    
    numeroReserva = input('Ingrese el número de reserva: ')
    fechaIngreso = input('Ingrese la fecha de ingreso: ')
    fechaSalida = input('Ingrese la fecha de salida: ')
    capacidad = validarNumero('la cantidad de huespedes: ')
    #idUsuario = input('Ingrese el ID del usuario: ')
    #idHuesped = input('Ingrese el ID del huésped: ')

    reserva = Reserva(numeroReserva, fechaIngreso, fechaSalida, capacidad,)

    dao = DAO()
    dao.registrarReserva(reserva)

    print('La reserva se registró correctamente:')
    print(reserva)

def registrarHuesped():
    rut = input('Ingrese el rut del huésped: ')
    nombre = input('Ingrese el nombre del huésped: ')
    edad = validarNumero('la edad del huésped: ')
    fechaIngreso = input('Ingrese la fecha de ingreso: ')
    fechaSalida = input('Ingrese la fecha de salida: ')
    #codigoHabitacion = input('Ingrese el código de la habitación: ')

    huesped = Huesped(rut, nombre, edad, fechaIngreso, fechaSalida,)

    dao = DAO()
    dao.registrarHuesped(huesped)

    print('El huésped se registró correctamente:')
    print(huesped)

lista_habitaciones = []
lista_tipos_habitacion = []
lista_tipos_usuario = []

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
        registrarHabitacion(lista_habitaciones)
    elif opcion == '3':
        registrarHuesped()
    elif opcion == '4':
        registrarTipoHabitacion(lista_tipos_habitacion)
    elif opcion == '5':
        registrarReserva()
    elif opcion =='6':
        registrarTipoUsuario(lista_tipos_usuario)
    elif opcion == '9':
        print('Salir')
        break
    else:
        print('La opción ingresada no es válida.')
        print('Ingrese una nueva opción.')