from Vehiculo import *#Importamos todo del modulo vehiculo
class Carga(Vehiculo):#Creamos una clase llamada carga y le asignamos como parametro el modulo vehiculo
    def __init__(self,placa,conductor,capacidad,ejes):#Creamos un metodo y inicializamos los parametros con __init__
        Vehiculo.__init__(self,placa,conductor)#Llamamos la clase vehiculo y inicializamos sus parametros
        self.__capacidad=capacidad#ponemos el parametro capacidad en privado 
        self.__ejes=ejes#LLamamos el parametro ejes el cual esta en privado    
    def getCapacidad(self):#Creamos otro pero esta vez para traer los atributos de el parametro capacidad
        return self.__capacidad#retornamos los atributos de capacidad    
    def getEjes(self):#Creamos otro metodo y esta vez llamamos los atributos de el parametro Ejes
        return self.__ejes#retornamos los atributos del parametro