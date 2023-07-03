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
    tipoUsuario = int(input("Ingrese 4 si es encargado o 5 si es administrador: "))

    for i in datos:
        while True:    
            if tipoUsuario == i[0]:  
                tipoUsuario = i[0]
                #print(tipoUsuario)
                usuario = Usuario(rut,nombre, usuario, password, edad,tipoUsuario, )
                dao = DAO()
                dao.registrarUsuario(usuario)
                break

            elif tipoUsuario== i[0]:
            
                tipoUsuario = i[0]
                #print(tipoUsuario)
                usuario = Usuario(rut,nombre, usuario, password, edad,tipoUsuario, )
                dao = DAO()
                dao.registrarUsuario(usuario)
                break
            #Validacion id no existe
            break
                
                






def registrarTipoUsuario(lista_tipos_usuario):
    
    while True:    
        nombreTipoUsuario = input('Ingrese si es Encargado o Administrador: ').lower()
    
        if nombreTipoUsuario == "encargado":
            tipoUsuario = TipoUsuario(nombreTipoUsuario, )
            dao = DAO()
            dao.registrarTipoUsuario(tipoUsuario)
            break
        elif nombreTipoUsuario == "administrador":

            tipoUsuario = TipoUsuario(nombreTipoUsuario,)
            dao = DAO()
            dao.registrarTipoUsuario(tipoUsuario)
            break
        else:
            print("Tipo de usuario invalido, intente nuevamente")
            

def registrarHabitacion(lista_habitaciones):

    dao= DAO()

    datosReserva = dao.obtenerIdReserva()
    datosTipoHabitacion= dao.obtenerIdTipoHabitacion()
    datosHuesped = dao.obtenerIdHuesped()

    numero = input('Ingrese el número de la habitación: ')


    orientacion = input('Ingrese la orientación de la habitación: ')
    ocupacion = input('Ingrese la ocupación de la habitación: ')
    respuesta= input("¿El cliente es encargado?(SI o NO)").lower()
    if respuesta =="si":
        idEncargado="si"
    else:
        idEncargado = "no"
    
    print(datosReserva)
    idReserva = int(input('Ingrese el ID de la reserva asociada: '))
    print(datosTipoHabitacion)
    idHabitacion = int(input('Ingrese el ID de la habitación asociada: '))
    print(datosHuesped)
    idHuesped = int(input('Ingrese el ID del huésped asociado: '))


    print(datosReserva)
    print(datosTipoHabitacion)
    print(datosHuesped)

    for i in datosReserva:
        while True:
            if idReserva == i[0]:
                idReserva = i[0]
                print(idReserva)
                for x in datosTipoHabitacion:
                    while True:    
                        if idHabitacion == x[0]:
                            idHabitacion = x[0]
                            print(idHabitacion)
                            for z in datosHuesped:
                                while True:
                                    if idHuesped == z[0]:
                                        idHuesped = z[0]
                                        print(idHuesped)
                                        habitacion = Habitacion(numero, orientacion,ocupacion,idEncargado,idReserva,idHabitacion,idHuesped,)
                                        dao.registrarHabitacion(habitacion)
                                        break
                                    break
                            break
                        break
                break
            break
            ##buscar manera de validar que si ingresa un valor que no existe en los datos lo vuelva a pedir

    print('La habitación se registró correctamente:')
    
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
    dao = DAO()
    datosHuesped = dao.obtenerIdHuesped()
    datosUsuario = dao.obtenerIdUsuario()
    numeroReserva = input('Ingrese el número de reserva: ')
    fechaIngreso = input('Ingrese la fecha de ingreso: ')
    fechaSalida = input('Ingrese la fecha de salida: ')
    capacidad = validarNumero('la cantidad de huespedes: ')
    print(datosUsuario)
    idUsuario = int(input("Ingrese el id del usuario: ")) 
    print(datosHuesped)
    idHuesped = int(input("Ingrese el id del huesped: "))

    

    for i in datosUsuario: 
        while True: 
            if idUsuario == i[0]:  
                idUsuario = i[0]
                print(idUsuario)
                for x in datosHuesped:
                    while True:
                        
                        if idHuesped == x[0]:
                            idHuesped = x[0]
                            print(idHuesped)
                            reserva = Reserva(numeroReserva,fechaIngreso,fechaSalida,capacidad,idUsuario,idHuesped,)
                            dao.registrarReserva(reserva)

                            print('La reserva se registró correctamente:')
                            break
                        break
                break
            break
        ##buscar manera de validar que si ingresa un valor que no existe en los datos lo vuelva a pedir
            



    


def registrarHuesped():
    dao = DAO() 
    datosHabitacion = dao.obtenerIdHabitacion()
    rut = input('Ingrese el rut del huésped: ')
    nombre = input('Ingrese el nombre del huésped: ')
    edad = validarNumero('la edad del huésped: ')
    fechaIngreso = input('Ingrese la fecha de ingreso (YYYY-MM-DD): ')
    fechaSalida = input('Ingrese la fecha de salida (YYYY-MM-DD): ')
    print(datosHabitacion)
    codigoHabitacion = int(input('Ingrese el código de la habitación: '))


    for i in datosHabitacion:
        while True:
            if codigoHabitacion == i[0]:
                codigoHabitacion = i[0]
                huesped = Huesped(rut,nombre,edad,fechaIngreso,fechaSalida,codigoHabitacion,)
                dao.registrarHuesped(huesped)
                break
            break
    
    print('El huésped se registró correctamente:')


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