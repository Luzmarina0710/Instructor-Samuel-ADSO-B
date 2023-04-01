from carga import *#Indicamos que del modulo cargar importe todo
from Conductor import *#Indicamos que del modulo conductor importe todo
# c1=Conductor('Luis',12345)
# carga1=Carga('aaa-123',c1,5,2)
# print(carga1)
nomConductor=input('Ingrese nombre del conductor')#Creamos una variable y le indicamos al usuario que ingrese un nombre
docConductor=int(input('Ingrese documento del conductor'))#Creamos una variable y le pedimos un numero de documento al usuario
placa=input('ingrese placa')#Creamos una variable llamada placa y le pedimos al usuario que ingrese la placa
capacidad=input('ingrese capacidad en toneladas')#Creamos una variable le inicidamos al usuario que digite una cantidad de toneladas
ejes=input('ingrese numero de ejes')#Creamos una nueva variable llamada ejes y le indicamos al usuario que ingrese una cantidad especifica de ejes
c1=Conductor(nomConductor,docConductor)#Creamos un objeto y le asignamos el modulo conductor y le agregamos la variable nomConductor y docConductor como parametros
obCarga=Carga(placa,c1,capacidad,ejes)#Creamos un obejto para carga y le asignamos el modulo cargar y le agregamos las variables restantes las cuales tienen informacion del usuario
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento())#Creamos una variable y le agreamos un objeto a el parametro carga,despues llamamos los atributos de el parametro conductor y lo mismo del parametro nombre despues lo concatenamos con el objeto carga y los atributos de conductor y documento

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes())#Creamos una variable para carga y le creamos un objeto

with open('poo-archivos/listado.txt','a') as flujo:#indicamos con open habra la sigiente direccion y le ponemos un alias
    flujo.write(cadCarga+'\n')#y aca ponemos en flujo el metodo write que indica escribir y lo concatenamos con \n para darle un salto de linea
