#Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

def grados_celsius():
    farenheit = float(input("Introduzca la cantidad de Farenheit: "))
    celsius = ((round(farenheit, 2)-32)*5)/9
    return (round(celsius, 2))

def main():
    farenheit = grados_celsius()
    print(f"Introducido {farenheit}ºF,serían {grados_celsius(farenheit)}ºC.")

if __name__ == '__main__':
    main()


