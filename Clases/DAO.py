import mysql.connector
import credenciales
from tipousuario import TipoUsuario

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
    
    