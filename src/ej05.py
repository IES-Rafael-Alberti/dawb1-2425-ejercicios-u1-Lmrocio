#Escribe un programa que pida el importe sin IVA de un artículo 
#y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

Igeneral = 1.21
Ireducido = 1.1
Isuperre = 1.04
SinI = 1


precio = float(input("Escriba el importe sin IVA del artículo: " ))

print("TIPOS DE IVA" )
print("IVA general (1.21)")
print("IVA reducido (1.1)")
print("IVA superreducido (1.04)")
print("No aplica IVA (1)" ) 

iva = float(input("Introduzca el IVA a aplicar: \n"))

print(f"El precio final es de: ", precio*iva)