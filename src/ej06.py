#Escribe un programa que pida el importe final de un artículo 
#y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA 
#(suponiendo que se ha aplicado un tipo de IVA del 10%).

iva = 1.1
total = float(input("Escriba el importe total del artículo:  "))

sinI = total/iva

print(f"El precio sin IVA es de ", sinI)