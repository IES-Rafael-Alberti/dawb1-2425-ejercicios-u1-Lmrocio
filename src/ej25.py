'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''

def datos_entrada():
    cumpleaños = input("Introduzca su cumpleaños en formato dd/mm/aaaa: ")
    cumpleaños_split = cumpleaños.split("/")
    if cumpleaños_split[0].count == 1:
        cumpleaños_split[0] = "0" + cumpleaños_split[0]
    if cumpleaños_split[1].count == 1:
        cumpleaños_split[1] = "0" + cumpleaños_split[1]
    return cumpleaños_split[0],cumpleaños_split[1],cumpleaños_split[2]

def main():
    dia,mes,año = datos_entrada()
    print(f"Su cumpleaños es el día {dia}, del mes {mes}, del año {año}.")

if __name__ == "__main__":
    main()