#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio

horas = int(input("Escriba las horas de trabajo: "))
coste_horas = float(input("Escriba el precio por hora: "))
print(f"El importe es: {horas * coste_horas}€ .")
