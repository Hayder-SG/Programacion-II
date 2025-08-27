from EcuacionLineal import EcuacionCuadratica

def main():
    print("Ingrese los coeficientes a, b y c de la ecuación cuadrática ax² + bx + c = 0:")

    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos.")
        return

    if a == 0:
        print("No es una ecuación cuadrática (a no puede ser 0).")
        return

    ecuacion = EcuacionCuadratica(a, b, c)
    d = ecuacion.getDiscriminante()

    if d > 0:
        r1 = ecuacion.getRaiz1()
        r2 = ecuacion.getRaiz2()
        print(f"La ecuación tiene dos raíces reales: r1 = {r1:.2f}, r2 = {r2:.2f}")
    elif d == 0:
        r = ecuacion.getRaiz1()  # r1 y r2 son iguales
        print(f"La ecuación tiene una única raíz real: r = {r:.2f}")
    else:
        print("La ecuación no tiene raíces reales.")

if __name__ == "__main__":
    main()
