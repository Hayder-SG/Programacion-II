class Persona:
    def __init__(self, nombre, edad, pesoPersona):
        self.__nombre = nombre
        self.__edad = edad
        self.__pesoPersona = pesoPersona

    def getPeso(self):
        return self.__pesoPersona

    def getEdad(self):
        return self.__edad

    def mostrar(self):
        print(self.__nombre, self.__edad, self.__pesoPersona)


class Cabina:
    def __init__(self, nroCabina):
        self.__nroCabina = nroCabina
        self.__personasAbordo = []

    def getNroCabina(self):
        return self.__nroCabina

    def agregarPersona(self, persona):
        peso = sum(p.getPeso() for p in self.__personasAbordo)
        if len(self.__personasAbordo) < 10 and peso + persona.getPeso() <= 850:
            self.__personasAbordo.append(persona)
        else:
            print("No se puede abordar la persona")

    def mostrar(self):
        print("Cabina:", self.__nroCabina)
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
    def __init__(self, color):
        self.__color = color
        self.__filaPersonas = []
        self.__cabinas = []

    def getColor(self):
        return self.__color

    def agregarCabina(self, cab):
        self.__cabinas.append(cab)

    def agregarPerFila(self, p):
        self.__filaPersonas.append(p)

    def agregarPersona(self):
        if not self.__filaPersonas or not self.__cabinas:
            return
        persona = self.__filaPersonas.pop(0)
        self.__cabinas[0].agregarPersona(persona)

    def mostrar(self):
        print("\nLínea:", self.__color)
        print("Personas en fila:")
        for p in self.__filaPersonas:
            p.mostrar()
        print("Cabinas:")
        for c in self.__cabinas:
            c.mostrar()

    def sumaLineas(self):
        return sum(c.cabinaTotal() for c in self.__cabinas)


class MiTeleferico:
    def __init__(self):
        self.__lineas = []

    def agregarLinea(self, linea):
        self.__lineas.append(linea)

    def mostrar(self):
        for l in self.__lineas:
            l.mostrar()

    def agregarPersonaFila(self, p, linea):
        for l in self.__lineas:
            if l.getColor() == linea.getColor():
                l.agregarPerFila(p)
                return

    def ingreso_total(self):
        total = sum(l.sumaLineas() for l in self.__lineas)
        print("Ingreso total:", total)


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

l2.agregarCabina(c1)

my = MiTeleferico()
my.agregarLinea(l1)
my.agregarLinea(l2)
my.agregarLinea(l3)

my.agregarPersonaFila(p1, l2)
my.agregarPersonaFila(p2, l2)

l2.agregarPersona()

my.mostrar()