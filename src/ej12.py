"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable,
y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal 
calculado redondeado con dos decimales
"""
peso = float(input("Escriba su peso en kilogramos: "))
altura = float(input("Escriba su altura en metros: "))

masa = peso / (altura*altura)
masa = round (masa, 2)

print(f"Tu índice de masa corporal es de: ", masa)