import math
class AlgebraVectorial:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, otro):
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    def __sub__(self, otro):
        return AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    def __mul__(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    def __xor__(self, otro):
        return AlgebraVectorial(self.y*otro.z - self.z*otro.y,
                    self.z*otro.x - self.x*otro.z,
                    self.x*otro.y - self.y*otro.x)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    # a)
    def perpendicular_a(self, otro):
        return abs(self + otro) == abs(self - otro)
    # b)
    def perpendicular_b(self, otro):
        return abs(self - otro) == abs(otro - self)
    # c)
    def perpendicular_c(self, otro):
        return self * otro == 0
    # d)
    def perpendicular_d(self, otro):
        return abs(self + otro)**2 == abs(self)**2 + abs(otro)**2
    # e)
    def paralelo_e(self, otro):
        if otro.x == 0 and otro.y == 0 and otro.z == 0:
            return False
        r = None
        for comp_a, comp_b in [(self.x, otro.x), (self.y, otro.y), (self.z, otro.z)]:
            if comp_b != 0:
                if r is None:
                    r = comp_a / comp_b
                elif abs(comp_a / comp_b - r) > 1e-9:
                    return False
            else:
                if comp_a != 0:
                    return False
        return True
    def paralelo_f(self, otro):
        return (self ^ otro).x == 0 and (self ^ otro).y == 0 and (self ^ otro).z == 0
    def proyeccion_sobre(self, otro):
        factor = (self * otro) / (abs(otro)**2)
        return AlgebraVectorial(otro.x * factor, otro.y * factor, otro.z * factor)
    def componente_en(self, otro):
        return (self * otro) / abs(otro)


a = AlgebraVectorial(2, 3, 0)
b = AlgebraVectorial(-3, 2, 0)
#vertores
print("vectores")
print("a =", a)
print("b =", b)
#insisos
print("a) Perpendicular (|a+b|=|a-b|):", a.perpendicular_a(b))
print("b) Perpendicular (|a-b|=|b-a|):", a.perpendicular_b(b))
print("c) Perpendicular (a·b=0):", a.perpendicular_c(b))
print("d) Perpendicular (|a+b|²=|a|²+|b|²):", a.perpendicular_d(b))
print("e) Paralelo (a=r·b):", a.paralelo_e(b))
print("f) Paralelo (a×b=0):", a.paralelo_f(b))
print("g) Proyección de a sobre b:", a.proyeccion_sobre(b))
print("h) Componente de a en b:", a.componente_en(b))


