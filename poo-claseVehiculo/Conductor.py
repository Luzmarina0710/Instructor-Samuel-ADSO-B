class Conductor:#Creamos una clase llamada Conductor
    def __init__(self,nombre,documento):#Creamos un metodo y inicializamos con __init__ y le agregamos dos parametros y con self indicamos que estamos dentro de la clase
        self.__nombre=nombre#Ponemos nombre en privado
        self.__documento=documento#Ponemos documento en privado
    def getNombre(self):#LLamamos los atributos de el parametro Nombre y le indicamos que estamos dentro
        return self.__nombre#Retornamos el contenido de el parametro nombre
    def getDocumento(self):#LLamamos los atributos de el parametro Documento e indicamos que estamos dentro
        return self.__documento#Retornamos el contenido del parametro documento
    