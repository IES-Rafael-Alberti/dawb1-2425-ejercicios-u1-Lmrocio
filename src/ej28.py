'''
Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

  - El segundo número no puede ser igual, si es así, debe mostrar el error: **"Los números no pueden ser iguales"**.
  - Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: **"El número menor es el 5 y entre ellos existen 7 números enteros"**.
'''
def compara_numeros(n1,n2):
    if n1 == n2:
        res = "Los números no puede ser iguales"
        return res
    elif n1 < n2:
        res = f"El número {n1} es menor que {n2} entre ellos existen {n2-n1-1} números enteros"
        return res
    else:
        res = f"El número {n2} es menor que {n1} entre ellos existen {n1-n2-1} números enteros"
        return res

def main():
    n1 = int(input("Introduzca el primer número: "))
    n2 = int(input("Introduzca el segundo número: "))
    print(compara_numeros(n1,n2))
    
if __name__ == "__main__":
    main()