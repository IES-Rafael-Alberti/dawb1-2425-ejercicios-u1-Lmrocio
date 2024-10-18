"""
4% de interés al año, se añaden al balance final. Escribir un programa que comience leyendo la cantidad de dinero depositada en 
la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
depo = float(input("Introduzca la cantidad de dinero depositada: "))
prim_año = depo*1.04
print(f"El ahorro durante el primer año será de: {round(prim_año, 2)}")
seg_año = prim_año * 1.04
print(f"El ahorro durante el segundo año será de: {round(seg_año, 2)}")
terc_año = seg_año*1.04
print(f"El ahorro durante el tercer año será de: {round(terc_año, 2)}")