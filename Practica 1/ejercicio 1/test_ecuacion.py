from ecuacion_lineal import EcuacionLineal

def main():
    print("Ingrese los valores para a, b, c, d, e, f:")
    
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        d = float(input("d: "))
        e = float(input("e: "))
        f = float(input("f: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos.")
        return

    ecuacion = EcuacionLineal(a, b, c, d, e, f)

    if ecuacion.tieneSolucion():
        x = ecuacion.getX()
        y = ecuacion.getY()
        print(f"La solución es: x = {x:.2f}, y = {y:.2f}")
    else:
        print("La ecuación no tiene solución (el determinante es 0).")

if __name__ == "__main__":
    main()
