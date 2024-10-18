'''
Escribir un programa que pregunte por consola el precio de un producto 
en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''
def datos_entrada():
    precio = float(input("Introduzca el precio del producto:"))
    return round(precio, 2)

def main():
    nuevo_precio = str(datos_entrada()).split(".")
    euros = nuevo_precio[0]
    centimos = "0," + nuevo_precio[1]
    print(f"Ha introducido {euros} euros y {centimos} céntimos.")

if __name__ == "__main__":
    main()