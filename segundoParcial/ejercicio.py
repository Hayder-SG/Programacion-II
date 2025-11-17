class Persona:
    def __init__(self, nombre, edad, pesoPersona):
        self.__nombre = nombre
        self.__edad = edad
        self.__persoPersona = pesoPersona
    def getPeso(self): 
        return self.__pesoPersona
    
    def mostrar(self):
        print(self.__nombre, self.__edad, self.__pesoPersona)
    
class Cabina:
    def __init__(self, nroCabina):
        self.__nroCabina = nroCabina
        self.__personasAbordo = []
    
    def getNroCavina(self):
        return self.getNroCavina

    
    def agregarPersona(self, persona):
        peso = 0
        for p in self.__personasAbordo:
            peso += p.getPeso()
        if len(self.__personasAbordo) <= 10 and peso + persona.getPeso() <= 850:
            self.__personasAbordo.append(persona)
        else:
            print("No se puede abordar la persona")
        
    def mostrar(self):
        print(self.__nroCabina)
        for p in self.__personasAbordo:
            p.mostrar()
    def cabinaTotal(self):
        total = 0
        for p in self.__personasAbordo:
            if p.getEdad() <= 18 or p.getEdad() >= 60:
                total += 1.50
            else:
                total += 3
        return total
        
class Linea:
    def __init__(self, color, cantidadCabinas = 0):
        self.__color = color
        self.__filaPersonas = []
        self.__cabinas = []
        self.__cantidadCabinas = cantidadCabinas
        
    def getColor(self):
        return self.__color
    def agregarPersona(self, p):
        self.__cabinas.append(p)
        self.__filaPersonas.pop(0)
    
    def agregarPerFila(self, p):
        self.__filaPersonas.append(p)
    
    def agregarCabina(self, nroCab):
        self.__cabinas.append(nroCab)
    
    def cantcabinas(self):
        return len(self.__cabinas)
    
    def mostrar(self):
        print(self.__color)
        print(self.__cantidadCabinas)
        for p in self.__filaPersonas:
            p.mostrar()
        for c in self.__cabinas:
            c.mostrar()
    
    def sumaLineas(self):
        total = 0
        for p in self.__filaPersonas:
            total += p.cabinaTotal()
        return total
    
class MiTeleferico:
    def __init__(self):
        self.__lineas = []
        self.__cantidadIngresos = 0
        
    def mostrar(self):
        for l in self.__lineas:
            l.mostrar()
            
    def agregarPersonaFila(self, p, linea):
        for lin in self.__lineas:
            lin.getLinea() 

    def ingreso_total(self):
        total = 0
        for l in self.__lineas:
            total += l.sumaLineas()
        print(total)

p1 = Persona("juan", 18, 50.1)
p2 = Persona("pepe", 16, 55.1)
p3 = Persona("maria", 19, 60.1)
p4 = Persona("carlos", 6, 26.1)        
        
c1 = Cabina(1)
c2 = Cabina(2)
c3 = Cabina(3)

l1 = Linea("rojo")
l2 = Linea("amarillo")
l3 = Linea("azul")

my = MiTeleferico()

my.agregarPersonaFila(p1, l2)