'''
Realiza un programa en Python que solicite un nombre y una edad.

  - Si el nombre está vacío, debes utilizar el valor **"Desconocido"**. La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
  - El programa mostrará la siguiente frase: **"Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir"**.

'''

def dato_nombre():
    nombre = input("Introduzca su nombre:")
    if nombre is None:
        nombre = "Desconocido"
    return nombre

def dato_edad():
    edad = -1
    while edad < 0 or edad > 125:
        edad = int(input("Introduzca su edad:"))
    return edad

def main():
    nombre = dato_nombre()
    edad = dato_edad()
    print (f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir.")

if __name__ == "__main__":
    main()