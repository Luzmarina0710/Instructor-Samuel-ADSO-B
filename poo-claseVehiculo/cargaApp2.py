from Conductor import *#Indicamos que del modulo Conductor importeme todo
from carga import *#Indicamos que del modulo carga importeme todo
lista=[]#creamos una lista vacia
with open('poo-archivos/listado.txt','r') as flujo:#Habrimos la direccion que esta dentro de open y le cambiamos el alias
    for ob in flujo:#ponemos un for para iterar flujo
        lista.append(ob)#Le agregamos a la lista la variable ob la cual tiene el contenido de flujo
i=0#creamos un contador
for ob in lista:#recorremos ob en lista
    lista[i]=ob.rstrip()#decimos que lista ya no esta vacia si no tiene el contenido de i,y ponemos un rstrip para eliminar los espacios de la derecha
    i+=1#Indicamos que cuando no se cumpla le sume uno al contador que en este caso es i
print(lista)#imprimimos la lista
#placa, nombre,doc, cap, ejes
lautos=[]#creamos otra lista vacia
for ob in lista:#recorremos ob en la lista(literal)
    #for x in ob.split(','):
    lautos.append(ob.split(','))#a la lista lautos le agregamos el objeto ob,y ponemos .split para convertir una cadena en una lista
cargas=[]#Creamos una nueva lista
print(lautos)#imprimimos la lista autos
for i in range(len(lautos)):#pedimos que i recorra todos los indices de la lista lautos
    #print(lautos[i][0])    
    p=lautos[i][0]#creamos varias variables y le agreamos a la lista lo que recorrio i en este caso desde i a la posicion 0
    n=lautos[i][1]#creamos varias variables y le agreamos a la lista lo que recorrio i en este caso desde i a la posicion 1
    d=lautos[i][2]#creamos varias variables y le agreamos a la lista lo que recorrio i en este caso desde i a la posicion 2
    c=lautos[i][3]#creamos varias variables y le agreamos a la lista lo que recorrio i en este caso desde i a la posicion 3
    e=lautos[i][4]#creamos varias variables y le agreamos a la lista lo que recorrio i en este caso desde i a la posicion 4
    con=Conductor(n,d)#creamos otra variable y le agregamos el modulo conductor para llamar las varibles n y d
    obj=Carga(p,con,c,e)#creamos un objeto y le agregamos el modulo carga con las variables restantes
    cargas.append(obj)#le agregamos a la variable obj el cual saldra al final
print(cargas)#Imprimimos el contenido de cargas
# 
# for ob in lautos:
    
#     #for x in ob:
#      #   print(x)
#         # p=x[0]
#         # n=x[1]
#         # d=x[2]
#         # c=x[3]
#         # e=x[4]
#         # con=Conductor(n,d)
#         # obj=Carga(p,con,c,e)
#         # cargas.append(obj)
# print(cargas)
