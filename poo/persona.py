class Persona:#Creamos una clase llamada Persona
    def __init__(self,nombre):#creamos un metodo para nuestra clase y le indicamos que estamos dentro de la clase con self,agregamos un parametro
        self.__nombre=nombre#Le agregamos nuestro parametro y lo ponemos en privado
        print('Activando constructor')#Mostramos por pantalla el string

    def getNombre(self):#Ponemos el metodo get para llamar los atributos
        return self.__nombre#retornamos el parametro nombre
    
    def setNombre(self, nombre):#Agregamos el metodo set para agregar un nombre
        self.__nombre=nombre#llamamos nuestro parametro

    def metodo(self):#creamo un nuevo metodo  y le indicamos un self
        print('Soy un método')#Imprimimos el string


ob=Persona('Ana')#Creamos un objeto para la clase persona
print(ob.getNombre())#Imprimimos el objeto y llamamos los atributos de nombre
ob.setNombre('Maria')#creamos un objeto y lo actualizamos el nombre "Ana" por "Maria"
print(ob.getNombre())#Imprimimos los atributos del parametro nombre
#ob.metodo()
#print(type(ob))