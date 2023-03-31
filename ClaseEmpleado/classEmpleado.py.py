class Empleado:
    def __init__(self,nombre, cargo, salario,hextras):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
        self.hextras=hextras
    def get_salario(self):
        return self.salario
    def get_nombre(self):
        return self.nombre
    def get_cargo(self):
        return self.cargo
    def get_hextras(self):
        return self.hextras
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def setsalario(self,salario):
        self.__salario=salario
    
    def setcargo(self,cargo):
        self.__cargo=cargo
    
    def sethextras(self,hextras):
        self.__hextras=hextras
    
    def Elminimo(self):
        if self.salario==1160000:
            incremento=self.__salario//100*16.3
            return incremento
        elif self.salario>1160000:
            incremento2=self.salario//100*13.3
            return incremento2
        elif self.__salario<1160000:
            return "Esta ganando menos que un minimo"
    
    def extra(self):
        if self.__hextras<11 and self.__extras>=0:
            total=self.__hextras*self.__salario//160
            return total
        elif self.__hextras>10 or self.__hextras<0:
            mensaje="Horas extras no mostradas"
            return mensaje
    
        
        
Empleado1=Empleado("juan","gerente de ventas",50000,2)  
print(Empleado1.get_salario())
print(Empleado1.get_nombre(),Empleado1.get_salario(),Empleado1.get_cargo(),Empleado1.get_hextras())

Empleado2=Empleado("paulo","supervisor",1800000,4)
print(Empleado1.salario)
print(Empleado2.get_nombre(),Empleado2.get_cargo(),Empleado2.get_salario(),Empleado2.Elminimo())