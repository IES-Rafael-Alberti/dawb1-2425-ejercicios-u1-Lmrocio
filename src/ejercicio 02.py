#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio

horas = int(input("Escriba las horas de trabajo: "))

precio = int(input("Escriba el precio por hora: "))

total = horas * precio

print(f"El importe total del servicio es: ", total)