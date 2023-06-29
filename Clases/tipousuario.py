class TipoUsuario:
    def __init__(self, idTipoUsuario,tipo):
        
        self.__tipo = tipo
        self.__idTipoUsuario = idTipoUsuario
    
    def getIdTipoUsuario(self):
        return self.__idTipoUsuario
    
    def setIdTipoUsuario(self, idTipoUsuario):
        self.__idTipoUsuario = idTipoUsuario
    
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def __str__(self):
        cadena = f'Tipo: {self.__tipo}'

        return cadena

