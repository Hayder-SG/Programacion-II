import random
class Juego:
    def __init__(self):
        self.numero_de_vidas = 0
        self.record = 0
    def reinicia_partida(self, vidas_iniciales=3):
        self.numero_de_vidas = vidas_iniciales
    def actualiza_record(self):
        if self.numero_de_vidas > self.record:
            self.record = self.numero_de_vidas
            print(f"¡Nuevo récord! Vidas restantes: {self.record}")
    def quita_vida(self):
        self.numero_de_vidas -= 1
        if self.numero_de_vidas > 0:
            print(f"Te quedan {self.numero_de_vidas} vidas.")
            return True
        else:
            print("No te quedan más vidas. ¡Perdiste!")
            return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas: int):
        super().__init__()
        self.numero_a_adivinar = 0
        self.reinicia_partida(vidas)
    def juega(self):
        self.numero_a_adivinar = random.randint(0, 10)
        self.reinicia_partida(self.numero_de_vidas)
        print("Adivina un número entre 0 y 10:")
        while True:
            try:
                intento = int(input("Tu intento: "))
            except ValueError:
                print("Debes ingresar un número entero.")
                continue
            if intento == self.numero_a_adivinar:
                print("¡Acertaste!")
                self.actualiza_record()
                break
            else:
                if not self.quita_vida():
                    break 
                else:
                    if intento < self.numero_a_adivinar:
                        print("El número a adivinar es mayor. Intenta de nuevo.")
                    else:
                        print("El número a adivinar es menor. Intenta de nuevo.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()
        swich = True
        while swich:
            print("si = 1, no = 2")
            volver_a_jugar = input("volver a jugar ¿si o no?: ")
            if volver_a_jugar=="si" or volver_a_jugar=="1":
                juego = JuegoAdivinaNumero(3)
                juego.juega()
            else:
                if volver_a_jugar=="no" or volver_a_jugar=="2":
                    swich = False
                    
Aplicacion.main()

