class TipoUsuario:
    def __init__(self, idTipoUsuario, tipo):
        self.__idTipoUsuario = idTipoUsuario
        self.__tipo = tipo
    
    def getIdTipoUsuario(self):
        return self.__idTipoUsuario
    
    def setIdTipoUsuario(self, idTipoUsuario):
        self.__idTipoUsuario = idTipoUsuario
    
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def __str__(self):
        return f"TipoUsuario: {self.__tipo}"
