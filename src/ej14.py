"""
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos 
y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
payaso = 112
muñeca = 75

numP = int(input("Introduzca el número de payasos vendidos: "))
numM = int(input("Introduzca el número de muñecas vendida: "))

print(f"El peso total del paquete será: {(numP*payaso)+(numM*muñeca)}.")