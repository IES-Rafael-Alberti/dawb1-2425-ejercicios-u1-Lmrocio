#Escribe un programa que pida el importe sin IVA de un artículo 
#y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.


def tipo_iva(tipo,precio):
    if tipo == "general":
        print(f"El precio total es {precio*1.21}")
    elif tipo == "reducido":
        print(f"El precio total es {precio*1.1}")
    elif tipo == "superreducido":
        print(f"El precio total es {precio*1.05}")
    elif tipo == "sin":
        print(f"El precio total es {precio*1}")
    else:
        print("No ha introducido un tipo valido")

def main():
    tipo = tipo_iva(input("Introduzca tipo de iva (general,reducido,superreducido,sin): "),int(input("Introduzca el precio sin IVA: ")))
if __name__ == "__main__":
    main()