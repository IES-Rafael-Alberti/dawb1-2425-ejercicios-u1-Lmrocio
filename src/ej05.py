#Escribe un programa que pida el importe sin IVA de un artículo 
#y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.


precio = float(input("Escriba el importe sin IVA del artículo: " ))
tipo = input("Introduzca tipo de iva (general,reducido,superreducido,sin): ")
if tipo == "general":
    print(f"Precio final{round(precio * 1.21, 2)}.")
elif tipo == "reducido":
    print(f"Precio final{round(precio * 1.1, 2)}.")
elif tipo == "superreducido":
    print(f"Precio final{round(precio * 1.04, 2)}.")
elif tipo == "sin":
    print(f"Precio final{round(precio * 1, 2) }.")
else:
    print("No se ha introducido un tipo valido.")