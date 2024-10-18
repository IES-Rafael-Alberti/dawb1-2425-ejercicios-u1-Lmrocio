#Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#Formatear la salida de los grados Farenheit a dos posiciones decimales.

cel = float(input("Escriba la temperatura en grados Celsius: "))
fah = ((cel * 9 )/5) + 32
print(f"Serían un total de {fah} grados Fahrenheit.")
print(f"Serían un total de {round(fah,2)} grados Fahrenheit.")
