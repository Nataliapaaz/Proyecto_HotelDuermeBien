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
        sql = "INSERT INTO tipoUsuario (tipo) VALUES (%s)"
        values = (tipoUsuario.getTipo(),)
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
        sql = "INSERT INTO usuario (rut, nombre, usuario, password, edad, idTipoUsuario_fk) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (usuario.getRut(),usuario.getNombre(),usuario.getUsuario(),usuario.getPassword(),usuario.getEdad(),usuario.getIdTipoUsuario(),)
        self.__cursor.execute(sql,values)
        self.fin()
    
    def registrarHabitacion(self, habitacion:Habitacion):
        self.inicio()
        sql = "INSERT INTO habitacion (numero,orientacion,ocupacion,idReserva_fk, idHabitacion_fk, idHuesped_fk) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (habitacion.getNumero(),habitacion.getOrientacion(),habitacion.getOcupacion(),habitacion.getIdReserva(),habitacion.getIdHabitacion(),habitacion.getIdHuesped(),)
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
        sql = "INSERT INTO reserva (numeroReserva, fechaIngreso, fechaSalida, capacidad, idUsuario_fk, idHuesped_fk) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (reserva.getNumeroReserva(),reserva.getFechaIngreso(),reserva.getFechaSalida(),reserva.getCapacidad(),reserva.getIdUsuario(),reserva.getIdHuesped(),)
        self.__cursor.execute(sql,values)
        self.fin()

    def obtenerTipos(self):
        self.inicio()
        sql = "SELECT * FROM tipousuario"
        self.__cursor.execute(sql)
        datos = self.__cursor.fetchall()
        self.fin()
        return datos
    
    def existeRutUsuario(self, rut):
        self.inicio()
        sql = "SELECT COUNT(*) FROM usuario WHERE rut = %s"
        self.__cursor.execute(sql,(rut,))
        count = self.__cursor.fetchone()[0]
        self.fin()
        return count>0
    
    def obtenerIdUsuario(self):
        self.inicio()
        sql = "SELECT * FROM usuario"
        self.__cursor.execute(sql)
        datos = self.__cursor.fetchall()
        self.fin()
        return datos
    
    def obtenerIdHuesped(self):
        self.inicio()
        sql = "SELECT * FROM huesped"
        self.__cursor.execute(sql)
        datos = self.__cursor.fetchall()
        self.fin()
        return datos
    
    def obtenerIdReserva(self):
        self.inicio()
        sql = "SELECT * FROM reserva"
        self.__cursor.execute(sql)
        datos = self.__cursor.fetchall()
        self.fin()
        return datos
    
    def obtenerIdHabitacion(self):
        self.inicio()
        sql = "SELECT * FROM tipohabitacion"
        self.__cursor.execute(sql)
        datos = self.__cursor.fetchall()
        self.fin()
        return datos
    