'''
Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

  - El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos *(os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)*.
  - Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: ***SERIE => 1-2..3..4..5..6..7..8..9-10***

'''

def datos_entrada():
    inicio = int(input("Introduzca un número de inicio: "))
    inc = int(input("Introduzca el incremento: "))
    total = int(input("Introduzca el final de la serie: "))
    if inc < 0:
        while inc < 0:
            inc = int(input("**ERROR** introduzca un incremento mayor que 0: "))
    if total < 0:
        while total < 0 :
            total = int(input("**ERROR** introduzca un total mayor que 0: "))
    return inicio, inc, total   
    
def suma_cadena(inicio,inc,total):
    res = ""
    res += str(inicio) + '-' + str(inicio+1)
    for i in range(inicio+2,total,inc):
        res += ".." + str(i)
    res += "-" + str(total)
    return res

def main():
    inicio, inc, total = datos_entrada()
    cadena = suma_cadena(inicio,inc,total)
    print(f"***SERIE => {cadena} ***")



if __name__ == "__main__":
    main()