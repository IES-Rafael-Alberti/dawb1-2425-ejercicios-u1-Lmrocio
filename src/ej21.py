'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
'''

frase = input("Introduzca una frase: ")
cadena = frase.split(' ')
cadena.reverse()
res = ""
for n in cadena:
   res += n + " "

print(res)