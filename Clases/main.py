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

#def obtenerTipoUsuario(idTipoUsuario):
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
    #print(datos)
    

    for i in datos:
        while True:  
            tipoUsuario = int(input("Ingrese 4 si es encargado o 5 si es administrador: "))  
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

            else:
                print("El id ingresado no existe, intente nuevamente")
            break
                
                






def registrarTipoUsuario(lista_tipos_usuario):
    
    while True:    
        nombreTipoUsuario = input('Ingrese si es Encargado o Administrador: ').lower()
    
# Validación de nombre de tipo de usuario repetido
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

    numero = input('Ingrese el número de la habitación: ')

# Validación de número de habitación repetido
    for habitacion in lista_habitaciones:
        if habitacion.getNumero() == numero:
            print('Error: El número de habitación ya existe.')
            return

    orientacion = input('Ingrese la orientación de la habitación: ')
    ocupacion = input('Ingrese la ocupación de la habitación: ')
    idReserva = int(input('Ingrese el ID de la reserva asociada: '))
    idHabitacion = int(input('Ingrese el ID de la habitación asociada: '))
    idHuesped = int(input('Ingrese el ID del huésped asociado: '))

    dao= DAO()

    datosReserva = dao.obtenerIdReserva()
    datosHabitacion= dao.obtenerIdHabitacion()
    datosHuesped = dao.obtenerIdHuesped()

    print(datosReserva)
    print(datosHabitacion)
    print(datosHuesped)

    for i in datosReserva:
        while True:
            if idReserva == i[0]:
                idReserva = i[0]
                print(idReserva)
                for x in datosHabitacion:
                    while True:    
                        if idHabitacion == x[0]:
                            idHabitacion = x[0]
                            print(idHabitacion)
                            for z in datosHuesped:
                                while True:
                                    if idHuesped == z[0]:
                                        idHuesped = z[0]
                                        print(idHuesped)
                                        habitacion = Habitacion(numero, orientacion,ocupacion,idReserva,idHabitacion,idHuesped,)
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
    
    numeroReserva = input('Ingrese el número de reserva: ')
    fechaIngreso = input('Ingrese la fecha de ingreso: ')
    fechaSalida = input('Ingrese la fecha de salida: ')
    capacidad = validarNumero('la cantidad de huespedes: ')
    idUsuario = int(input("Ingrese el id del usuario: ")) 
    idHuesped = int(input("Ingrese el id del huesped: "))
    dao = DAO()
    datosHuesped = dao.obtenerIdHuesped()
    datosUsuario = dao.obtenerIdUsuario()
    print(datosHuesped)
    

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
    rut = input('Ingrese el rut del huésped: ')
    nombre = input('Ingrese el nombre del huésped: ')
    edad = validarNumero('la edad del huésped: ')
    fechaIngreso = input('Ingrese la fecha de ingreso (YYYY-MM-DD): ')
    fechaSalida = input('Ingrese la fecha de salida (YYYY-MM-DD): ')
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