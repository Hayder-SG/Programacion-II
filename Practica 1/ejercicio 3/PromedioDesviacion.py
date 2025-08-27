import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros):
    media = promedio(numeros)
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    return math.sqrt(suma_cuadrados / (len(numeros) - 1))

def main():
    print("Ingrese 10 números separados por espacios:")

    while True:
        entrada = input(">>> ")
        try:
            lista = list(map(float, entrada.split()))
            if len(lista) != 10:
                print("Debe ingresar exactamente 10 números. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, asegúrese de ingresar solo números válidos.")

    media = promedio(lista)
    desvest = desviacion(lista)

    print(f"\nPromedio = {media:.2f}")
    print(f"Desviación estándar = {desvest:.2f}")

if __name__ == "__main__":
    main()
