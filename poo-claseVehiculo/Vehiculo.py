class Vehiculo:#Creamos una nueva clase llamada Vehiculo
    def __init__(self,placa,conductor):#Creamos un metodo para agregar dos parametros e inicializarlos con __init__
        self.__placa=placa#Ponemos en privado el parametro placa
        self.__conductor=conductor#Ponemos en privado el parametro conductor
    def getConductor(self):#LLamamos los atributos de el parametro conductor
        return self.__conductor#Retornamos los atributos de el parametro Conductor
    def getPlaca(self):#LLamamos los atributos de el parametro Placa
        return self.__placa#Retornamos los atributos del parametro placa