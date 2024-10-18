'''
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena 
con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
el número de unidades con tres dígitos y
el coste total con 8 dígitos enteros y 2 decimales.
'''

def datos_de_entrada():
    nombre = input("Introduzca el nombre del producto: ")
    precio = float(input("Introduzca el precio por unidad: "))
    cantidad = int(input("Introduzca la cantidad de productos: "))

    return nombre, precio, cantidad

def cadena(nombre, precio, cantidad):
    res =' '
    res = "El producto " + nombre + ", tiene el precio de " + str(round(precio, 2)) + " y son " + str(cantidad) + " unidades."
    return res

def main():
    nombre, precio, cantidad = datos_de_entrada()
    res = cadena(nombre, precio, cantidad)

    print(res)

if __name__ == '__main__':
    main()