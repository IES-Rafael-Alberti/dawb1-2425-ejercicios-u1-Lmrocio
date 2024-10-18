'''
Escribir un programa que pida al usuario que introduzca una frase en la consola
y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

def datos_entrada():
    frase = input("Introduzca una frase: ")
    vocal = input("Introduzca una vocal: ")

    return frase, vocal

def cambiar_frase(frase: str, vocal: str):
    frase = frase.replace(vocal, vocal.upper())

    return frase


def main():
    frase, vocal = datos_entrada()
    print(cambiar_frase(frase, vocal))

if __name__ == "__main__":
    main()