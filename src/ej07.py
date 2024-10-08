#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def Suma_de_3 ():
    num1 = float(input("Escribe el primer número: "))
    num2 = float(input("Escribe el segundo número: "))
    num3 = float(input("Escribe el tercer número: "))
    print(f"La suma de los tres números es: {num1+num2+num3}.")
    return ()

def main():
    Suma_de_3()

if __name__ == "__main__":
    main()
