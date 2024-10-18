'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola
y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''
def datos_entrada():
    correo = input("Introduzca un correo electrónico:")
    return correo

def main():
    correo_split = datos_entrada().split("@")
    correo_split[1] = "ceu.es."
    res = correo_split[0] + "@"+ correo_split[1]
    print(f"Su nuevo correo es: {res}")
if __name__ == "__main__":
    main()