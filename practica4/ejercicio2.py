from abc import ABC, abstractmethod
import random
import math
class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self):
        pass
class Figura(ABC):
    def __init__(self, color: str):
        self.color = color

    def set_color(self, color: str):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"Figura de color {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado de lado {self.lado}, color {self.color}"
class Circulo(Figura):
    def __init__(self, radio: float, color: str):
        super().__init__(color)
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo de radio {self.radio}, color {self.color}"
def main():
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Negro"]
    figuras = []

    for i in range(5):
        tipo = random.randint(1, 2) 
        color = random.choice(colores)
        if tipo == 1:
            lado = random.randint(1, 10)
            figuras.append(Cuadrado(lado, color))
        else:
            radio = random.randint(1, 10)
            figuras.append(Circulo(radio, color))

    print("\n--- Figuras Generadas ---")
    for fig in figuras:
        print(fig)
        print(f"Área: {fig.area():.2f}, Perímetro: {fig.perimetro():.2f}")

        if isinstance(fig, Coloreado): 
            print("Instrucción:", fig.como_colorear())
        print("-" * 40)
if __name__ == "__main__":
    main()
