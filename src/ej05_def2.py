"""
* *ej05_**def2**.py* => La función `calcula_precio(importe: float, iva: float) -> str` recibe el importe y 
el iva, si el iva está fuera del rango 0-100 se aplicará el 21%, y retornará una cadena de caracteres con el iva 
y el precio con iva mostrando solo 2 posiciones decimales. Ejemplo: calcula_precio(100, 21) -> 
"El precio final del artículo con IVA (21.00) es 121.00€."
"""

def calcula_precio(importe: float, iva: float):
    if iva < 0 or iva > 100:
        iva = 1.21
    else: 
        iva = (iva/100) + 1
        
    
    precio = round(importe * iva)
    return  iva, precio


def main():
    importe = float(input("Introduce el immporte a aplicar IVA: "))
    iva = float(input("Introduce el IVA a aplicar: "))
    
    iva, precio = calcula_precio(importe, iva)
 
    print(f"El precio final del artículo con IVA ({iva}) es {precio}.")

if __name__ == "__main__":
    main()