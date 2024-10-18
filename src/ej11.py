#Escribir un programa que lea un entero positivo, n, introducido por el usuario 
#y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
#La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

num = int(input("Escriba un número: "))
print(f"La suma desde 1 hasta {num} es: {sum(range(1,num+1))}.")