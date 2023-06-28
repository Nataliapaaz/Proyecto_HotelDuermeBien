import mysql.connector
import credenciales

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
    