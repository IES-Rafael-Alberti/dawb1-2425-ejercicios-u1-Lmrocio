"""
*ej04_**def2**.py* => La función `grados_celsius(farenheit: float) -> float` 
recibe los grados farenheit (redondeados a dos posiciones decimales) y retorna los grados celsius (redondeados a dos posiciones).
"""
def grados_celsius(farenheit):
    celsius = ((round(farenheit, 2)-32)*5)/9
    return (round(celsius, 2))

def main():
    farenheit = float(input("Introduzca la cantidad de Farenheit: "))
    grados_celsius(farenheit)
    print(f"Serían {grados_celsius(farenheit)} grados Celsius.")

if __name__ == '__main__':
    main()
