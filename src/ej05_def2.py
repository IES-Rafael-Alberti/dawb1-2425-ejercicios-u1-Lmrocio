"""
* *ej05_**def2**.py* => La función `calcula_precio(importe: float, iva: float) -> str` recibe el importe y 
el iva, si el iva está fuera del rango 0-100 se aplicará el 21%, y retornará una cadena de caracteres con el iva 
y el precio con iva mostrando solo 2 posiciones decimales. Ejemplo: calcula_precio(100, 21) -> 
"El precio final del artículo con IVA (21.00) es 121.00€."
"""

def calcula_precio(importe, iva):
    if iva < 0 or iva > 100:
        total = importe * 1.21
    else:
        total = importe * iva

def main():
    importe = float(input("Introduzca el importe: "))
    iva = float(input("Introduzca el iva ha aplicar: "))
    calcula_precio()

if __name__ == '__main__':
    main()