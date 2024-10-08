#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

def Suma_de_3():
    num1 = float(input("Escriba un número: "))
    num1 += float(input("Escriba otro número: "))
    num1 += float(input("Escriba otro número: "))
    print(f"La suma de los tres números es: {num1}.")
    return()

def main():
    Suma_de_3()

if __name__ == "__main__":
    main()

