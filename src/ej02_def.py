#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio

def salario(horas, coste_horas):
    return horas * coste_horas

def main():
    horas = int(input("Escriba las horas de trabajo: "))
    coste_horas = float(input("Escriba el precio por hora: "))
    print(f"El importe es: {salario(horas, coste_horas)}€ .")

if __name__ == "__main__":
    main()