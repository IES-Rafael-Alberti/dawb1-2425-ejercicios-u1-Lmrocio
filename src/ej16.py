"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante),
el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
"""

precio = 3.49

num_nodia = int(input("Introduzca la cantidad de pan vendido que no son del día: "))
descuento = precio*0.6
total = num_nodia*(precio-descuento)
print(f"La barra de pan cuesta {precio} al que se le aplica un descuento de {round(descuento, 2)} por barra, quedando un total de: {round(total, 2)}.")
