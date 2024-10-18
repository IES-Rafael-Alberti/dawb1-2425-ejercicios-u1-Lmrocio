import math

def calcular_area(a: float, b: float, c: float) -> float:
    semiper = (a + b + c)/2
    area = math.sqrt(semiper*(semiper-a)*(semiper-b)*(semiper-c))
    return (area)



def comprobar_triangulo_valido(a,b,c): #parte de la fórmula matemática, para no encontrar triángulos que no cierren
    return (a + b > c) and (a + c > b) and (b + c > a)



def comprobar_float(cadena: str) -> bool:
    if cadena.startswith("-"): #-88.78
        cadena = cadena[1:] #le quitamos el guión, seria 88.78

    pos_punto = cadena.find(".") #le quitamos el punto, buscamos que sean dígitos si tenemos 88.78
    if pos_punto >= 0:
       cadena = cadena[:pos_punto] + cadena[pos_punto + 1:] #nos quedaría 8878

    return cadena.isdigit()


def introduce_numero(msj: str) -> float:
    cadena = input(msj).strip().replace(",", ".") #le quitamos los espacios a los lados y cambiamos la coma por punto
    
    while (comprobar_float(cadena) == False):
        print("\n ***ERROR*** Número inválido.")
        cadena = input(msj).strip().replace(",", ".")

    return float(cadena)


def main():
    print("Dame los tres lados del triángulo.")
    lado_a = introduce_numero("Lado 1: ")
    lado_b = introduce_numero("Lado 2: ")
    lado_c = introduce_numero("Lado 3: ")

    if comprobar_triangulo_valido(lado_a,lado_b,lado_c):
        area = calcular_area(lado_a, lado_b, lado_c)
        print(f"El área del triángulos con los lados {round(lado_a, 2)}, {round(lado_b, 2)} y {round(lado_c, 2)} es {round(area, 2)}.")
    else:
        print(f"El triángulo con lados {lado_a}, {lado_b} y {lado_c} es inválido.")



if __name__ == '__main__':
    main()