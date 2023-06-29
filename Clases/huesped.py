class Huesped:
    def __init__(self, rut, nombre, edad, fechaIngreso, fechaSalida,idHuesped=-1):
        self.__idHuesped = idHuesped
        self.__rut = rut
        self.__nombre = nombre
        self.__edad = edad
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        ##self.__codigoHabitacion = codigoHabitacion
    
    def getIdHuesped(self):
        return self.__idHuesped
    
    def setIdHuesped(self, idHuesped):
        self.__idHuesped = idHuesped
    
    def getRut(self):
        return self.__rut
    
    def setRut(self, rut):
        self.__rut = rut
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad = edad
    
    def getFechaIngreso(self):
        return self.__fechaIngreso
    
    def setFechaIngreso(self, fechaIngreso):
        self.__fechaIngreso = fechaIngreso
    
    def getFechaSalida(self):
        return self.__fechaSalida
    
    def setFechaSalida(self, fechaSalida):
        self.__fechaSalida = fechaSalida
    
    #def getCodigoHabitacion(self):
    #    return self.__codigoHabitacion
    
    #def setCodigoHabitacion(self, codigoHabitacion):
    #    self.__codigoHabitacion = codigoHabitacion
    
    def __str__(self):
        cadena = ""
        cadena += f"Rut: {self.__rut}\n"
        cadena += f"Nombre: {self.__nombre}\n"
        cadena += f"Edad: {self.__edad}\n"
        cadena += f"Fecha de Ingreso: {self.__fechaIngreso}\n"
        cadena += f"Fecha de Salida: {self.__fechaSalida}\n"
        return cadena
