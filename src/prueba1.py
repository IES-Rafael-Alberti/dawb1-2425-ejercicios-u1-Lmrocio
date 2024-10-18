
def comparacion_num(num1, num2):

    if num1 < num2:
        return(num2)
    
    elif num1 > num2:
        return(num1)
    
    else:
        return 0

def main():
    num1= float(input("Introduzca un número: "))
    num2= float(input("Introduzca otro número: "))
    c = comparacion_num(num1, num2)
    print (c)


if __name__ == "__main__":
    main()
