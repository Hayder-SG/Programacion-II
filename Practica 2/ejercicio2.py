import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __rmul__(self, r):
        return Vector(r * self.x, r * self.y, r * self.z)
    def __mul__(self, otro):
        if isinstance(otro, Vector):
            return self.x*otro.x + self.y*otro.y + self.z*otro.z
        else:
            return Vector(self.x * otro, self.y * otro, self.z * otro)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normal(self):
        mag = abs(self)
        if mag == 0:
            raise ValueError("No se puede normalizar un vector nulo.")
        return Vector(self.x/mag, self.y/mag, self.z/mag)
    def producto_escalar(self, otro):
        return self * otro
    def cruz(self, otro):
        return Vector(self.y*otro.z - self.z*otro.y,
                        self.z*otro.x - self.x*otro.z,
                        self.x*otro.y - self.y*otro.x)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("2 * a =", 2 * a)
print("|a| =", abs(a))
print("Normal de a =", a.normal())
print("a · b =", a.producto_escalar(b))
print("a × b =", a.cruz(b))

