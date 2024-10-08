#¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

def Suma_de_3():
    print(f"El resultado es: {int(input("Escriba un número: ")) + int(input("Escriba otro número: ")) + int(input("Escriba otro número:  "))}")
    return()

def main():
    Suma_de_3()

if __name__ == "__main__":
    main()