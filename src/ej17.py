"""
Escribir un programa que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla en líneas distintas el nombre 
del usuario tantas veces como el número introducido.
"""
nombre = input("Introduzca un nombre: ")
num = int(input("Introduzca un número: "))

for i in range(1, num +1):
    print(nombre)

