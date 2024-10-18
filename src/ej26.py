'''
Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
'''

def datos_entrada():
    compra = input("Introduzca los productos de la cesta de la compra: ")
    compra_split = compra.split(',')
    return compra_split

def main():
    compra = datos_entrada()
    print("Los productos son: ")
    for n in compra:
        print("-" + n)



if __name__ == "__main__":
    main()