#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.
#Hecho con funciones para practicar

def suma_de_3 ():
    num1 = float(input("Escribe el primer número: "))
    num2 = float(input("Escribe el segundo número: "))
    num3 = float(input("Escribe el tercer número: "))
    return num1 + num2 + num3

def main():
    print(f"La suma de los tres números es: {round(suma_de_3(), 2)}.")
if __name__ == "__main__":
    main()

