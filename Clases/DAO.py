import mysql.connector
import credenciales
from tipousuario import TipoUsuario
from tipohabitacion import TipoHabitacion
from usuario import Usuario
from habitacion import Habitacion
from huesped import Huesped
from reserva import Reserva




class DAO():
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

        
    def inicio(self):
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()

        
    def fin(self):
        self.__conexion.commit()
        self.__conexion.close()
    

    def registrarTipoUsuario(self,tipoUsuario:TipoUsuario):
        self.inicio()
        sql = "INSERT INTO tipoUsuario (idTipoUsuario,tipo) VALUES (%s,%s)"
        values = (tipoUsuario.getIdTipoUsuario(),tipoUsuario.getTipo())
        self.__cursor.execute(sql,values)
        self.fin()
    
    def registrarTipoHabitacion(self, tipoHabitacion:TipoHabitacion,):
        self.inicio()
        sql = "INSERT INTO tipohabitacion (numeroCamas,numeroPasajeros) VALUES (%s,%s)"
        values = (tipoHabitacion.getNumeroCamas(),tipoHabitacion.getNumeroPasajeros(),)
        self.__cursor.execute(sql,values)
        self.fin()
    
    def registrarUsuario(self, usuario:Usuario):
        self.inicio()
        sql = "INSERT INTO usuario (rut, nombre, usuario, password, edad) VALUES (%s,%s,%s,%s,%s)"
        values = (usuario.getRut(),usuario.getNombre(),usuario.getUsuario(),usuario.getPassword(),usuario.getEdad(),)
        self.__cursor.execute(sql,values)
        self.fin()
    
    def registrarHabitacion(self, habitacion:Habitacion):
        self.inicio()
        sql = "INSERT INTO habitacion (numero,orientacion,ocupacion,idReserva, idHabitacion, idHuesped) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (habitacion.getNumero(),habitacion.getOrientacion(),habitacion.getOcupacion(),habitacion.getIdReserva(),habitacion.getIdHabitacion(),habitacion.getIdHuesped())
        self.__cursor.execute(sql,values)
        self.fin()

    def registrarHuesped(self, huesped:Huesped):
        self.inicio()
        sql = "INSERT INTO huesped (rut, nombre, edad, fechaIngreso, fechaSalida) VALUES (%s,%s,%s,%s,%s)"
        values = (huesped.getRut(),huesped.getNombre(),huesped.getEdad(),huesped.getFechaIngreso(),huesped.getFechaSalida(),)
        self.__cursor.execute(sql,values)
        self.fin()

    def registrarReserva(self, reserva:Reserva):
        self.inicio()
        sql = "INSERT INTO reserva (numeroReserva, fechaIngreso, fechaSalida, capacidad) VALUES (%s,%s,%s,%s)"
        values = (reserva.getNumeroReserva(),reserva.getFechaIngreso(),reserva.getFechaSalida(),reserva.getCapacidad(),)
        self.__cursor.execute(sql,values)
        self.fin()

    def obtenerTipos(self):
        self.inicio()
        sql = "SELECT * FROM tipousuario"
        self.__cursor.execute(sql)
        datos = self.__cursor.fetchall()
        self.fin()
        return datos