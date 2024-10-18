#Escribir un programa que lea un entero positivo, n, introducido por el usuario 
#y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
#La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:


def suma_final(num):
    suma = sum(range(1,num+1))
    return suma


def main():
    num = int(input("Introduzca un número: "))
    suma = suma_final(num)
    print(f"La suma del rango desde 1 hasta {num} es: {suma}.")


if __name__ == "__main__":
    main()