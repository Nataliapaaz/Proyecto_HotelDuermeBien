class Reserva:
    def __init__(self, numeroReserva, fechaIngreso, fechaSalida, capacidad,idUsuario, idHuesped, idReserva = -1):
        self.__idReserva = idReserva
        self.__numeroReserva = numeroReserva
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        self.__capacidad = capacidad
        self.__idUsuario = idUsuario
        self.__idHuesped = idHuesped
    
    def getIdReserva(self):
        return self.__idReserva
    
    def setIdReserva(self, idReserva):
        self.__idReserva = idReserva
    
    def getNumeroReserva(self):
        return self.__numeroReserva
    
    def setNumeroReserva(self, numeroReserva):
        self.__numeroReserva = numeroReserva
    
    def getFechaIngreso(self):
        return self.__fechaIngreso
    
    def setFechaIngreso(self, fechaIngreso):
        self.__fechaIngreso = fechaIngreso
    
    def getFechaSalida(self):
        return self.__fechaSalida
    
    def setFechaSalida(self, fechaSalida):
        self.__fechaSalida = fechaSalida
    
    def getCapacidad(self):
        return self.__capacidad
    
    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad
    
    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
    
    def getIdHuesped(self):
        return self.__idHuesped
    
    def setIdHuesped(self, idHuesped):
        self.__idHuesped = idHuesped
    
    def __str__(self):
        cadena = ""
        cadena += f"ID Reserva: {self.__idReserva}\n"
        cadena += f"Número de Reserva: {self.__numeroReserva}\n"
        cadena += f"Fecha de Ingreso: {self.__fechaIngreso}\n"
        cadena += f"Fecha de Salida: {self.__fechaSalida}\n"
        cadena += f"Huespedes Asociados: {self.__capacidad}\n"
        cadena += f"ID Usuario: {self.__idUsuario}\n"
        cadena += f"ID Huésped: {self.__idHuesped}\n"
        return cadena

