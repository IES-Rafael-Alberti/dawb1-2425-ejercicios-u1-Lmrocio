#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.
#Hecho con funciones para practicar.
def suma_de_3():
    num1 = float(input("Escriba un número: "))
    num1 += float(input("Escriba otro número: "))
    num2 = float(input("Escriba otro número: "))
    return num1+num2

def main():
    print(f"La suma de los tres números es: {round(suma_de_3(),2)}.")

if __name__ == "__main__":
    main()

