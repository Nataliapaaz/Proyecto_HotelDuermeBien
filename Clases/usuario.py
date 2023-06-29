class Usuario:
    def __init__(self, idUsuario, rut, nombre, usuario, password, edad, idTipoUsuario):
        self.__idUsuario = idUsuario
        self.__rut = rut
        self.__nombre = nombre
        self.__usuario = usuario
        self.__password = password
        self.__edad = edad
        self.__idTipoUsuario = idTipoUsuario
    
    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
    
    def getRut(self):
        return self.__rut
    
    def setRut(self, rut):
        self.__rut = rut
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getUsuario(self):
        return self.__usuario
    
    def setUsuario(self, usuario):
        self.__usuario = usuario
    
    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password
    
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad = edad
    
    def getIdTipoUsuario(self):
        return self.__idTipoUsuario
    
    def setIdTipoUsuario(self, idTipoUsuario):
        self.__idTipoUsuario = idTipoUsuario
    
    def __str__(self):
        cadena = ''
        cadena += f'Nombre: {self.__nombre}\n'
        cadena += f'Usuario: {self.__usuario}\n'
        cadena += f'Password: {self.__password}\n'
        cadena += f'Rut: {self.__rut}\n'
        cadena += f'Edad: {self.__edad}\n'
        cadena += f'Tipo Usuario: {self.__idTipoUsuario}\n'
        return cadena

