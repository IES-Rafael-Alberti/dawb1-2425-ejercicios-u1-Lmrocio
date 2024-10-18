'''
Suponiendo que se han ejecutado las siguientes sentencias de asignación: ancho = 17 y alto = 12.0
Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:

1. ancho / 2
2. ancho // 2
3. alto / 3
4. 1 + 2 * 5
Ejercicios adicionales:
5. `ancho * alto`
6. `(5 + 1) * 3`
7. `(5 + 1) / 3`
'''

ancho = 17
alto =12.0

division = ancho / 2
print(f"ancho / 2 = {division} y es de tipo {type(division)}")
division2 = ancho // 2
print(f"ancho // 2 = {division2} y es de tipo {type(division2)}")
division3 = alto / 3
print(f"alto / 3 = {division3} y es de tipo {type(division3)}")
res = 1 + 2 * 5
print(f"1 + 2 * 5 = {res} y es de tipo {type(res)}")
print(f"ancho * alto = {ancho * alto} y es de tipo {type(ancho * alto)}")
print(f"(5 + 1) * 3 = {(5 + 1) * 3} y es de tipo {type((5 + 1) * 3)}")
print(f"(5 + 1) / 3 = {(5 + 1) / 3} y es de tipo {type((5 + 1) / 3)}")