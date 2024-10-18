#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

def saludo(nombre):
    return (f"Hola, {nombre}.")

def main():
    print (saludo(input("Escriba su nombre: ")))
    
if __name__=="__main__":
    main()
