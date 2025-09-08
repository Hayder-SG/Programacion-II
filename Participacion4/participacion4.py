import math

class Circulo2D:
    def __init__(self, x=0, y=0, radio=1):
        self.x = x
        self.y = y
        self.radio = radio

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadio(self):
        return self.radio

    def getArea(self):
        return math.pi * self.radio**2

    def getPerimetro(self):
        return 2 * math.pi * self.radio

    def contiene(self, x=None, y=None, circulo=None):
        if x is not None and y is not None:
            distancia = math.sqrt((x - self.x)**2 + (y - self.y)**2)
            return distancia <= self.radio

        elif circulo is not None and isinstance(circulo, Circulo2D):
            distancia = math.sqrt((circulo.x - self.x)**2 + (circulo.y - self.y)**2)
            return distancia + circulo.radio <= self.radio

        else:
            raise ValueError("Debes pasar un punto (x, y) o un círculo Circulo2D")

    def sobrepone(self, circulo):
        distancia = math.sqrt((circulo.x - self.x)**2 + (circulo.y - self.y)**2)
        return distancia <= self.radio + circulo.radio


if __name__ == "__main__":
    c1 = Circulo2D(2, 0, 1)

    print("Área de c1:", c1.getArea())
    print("Perímetro de c1:", c1.getPerimetro())

    # Probar contiene con punto
    print("c1.contiene(x=2.5, y=0):", c1.contiene(x=2.5, y=0))

    # Probar contiene con círculo
    c2 = Circulo2D(2, 0, 0.5)
    print("c1.contiene(circulo=c2):", c1.contiene(circulo=c2))

    # Probar sobrepone
    c3 = Circulo2D(0, 0, 2)
    print("c1.sobrepone(c3):", c1.sobrepone(c3))
