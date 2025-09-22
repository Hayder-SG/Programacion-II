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
    def quita_vida(self) -> bool:
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
    def valida_numero(self, num: int) -> bool:
        """Valida que el número esté entre 0 y 10"""
        return 0 <= num <= 10
    def juega(self):
        self.reinicia_partida(self.numero_de_vidas)
        self.numero_a_adivinar = random.randint(0, 10)
        print("\n--- Juego Adivina Número ---")
        print("Adivina un número entre 0 y 10:")
        while True:
            try:
                intento = int(input("Tu intento: "))
            except ValueError:
                print("Debes ingresar un número entero.")
                continue
            if not self.valida_numero(intento):
                print("Número inválido. Intenta de nuevo.")
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
                        print("El número a adivinar es mayor.")
                    else:
                        print("El número a adivinar es menor.")
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def valida_numero(self, num: int):
        if 0 <= num <= 10:
            if num % 2 == 0:
                return True
            else:
                print("Error: Debes ingresar un número PAR entre 0 y 10.")
                return False
        return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def valida_numero(self, num: int) -> bool:
        if 0 <= num <= 10:
            if num % 2 != 0:
                return True
            else:
                print("Error: Debes ingresar un número IMPAR entre 0 y 10.")
                return False
        return False
class Aplicacion:
    @staticmethod
    def main():
        juegos = [
            JuegoAdivinaNumero(3),
            JuegoAdivinaPar(3),
            JuegoAdivinaImpar(3)
        ]
        for juego in juegos:
            juego.juega()
        swich = True
        while swich:
            print("si = 1, no = 2")
            volver_a_jugar = input("volver a jugar ¿si o no?: ")
            if volver_a_jugar=="si" or volver_a_jugar=="1":
                juegos = [
                JuegoAdivinaNumero(3),
                JuegoAdivinaPar(3),
                JuegoAdivinaImpar(3)
                ]
                for juego in juegos:
                    juego.juega()
            else:
                if volver_a_jugar=="no" or volver_a_jugar=="2":
                    swich = False

Aplicacion.main()
