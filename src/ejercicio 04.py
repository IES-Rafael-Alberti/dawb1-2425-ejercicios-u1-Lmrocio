#Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

cel = int(input("Escriba la temperatura en grados Celsius: "))

fah = ((cel * 9 )/5) + 32

print(f"Serían un total de ", fah, "grados Fahrenheit.")