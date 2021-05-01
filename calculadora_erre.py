import time as t
# Definimos colores para el logo
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
# Hasta aca
print(RED + "██████╗")
print(RED + "██╔══██╗")
print(RED + "██████╔╝")
print(RED + "██╔══██╗")
print(RED + "██║  ██║")
print(RED + "╚═╝  ╚═╝")
print(RESET + "\nBienvenidos, yo soy ERRRE y esta calculadora esta realizada por mi, disfrutenla.")
t.sleep(1.5)
operacion_numero = 1
print("\nLos operadores validos para esta calculadora son +, -, *, **, /")
t.sleep(1.5)
print("\nPara iniciar la calculadora ingresa el numero [1] y para salir ingresa [2]")
t.sleep(1.5)
op2 = input("\nIngresa la opcion: ")
while op2 == "1":
    if op2 == "2":
        break
    print("\nOperacion numero " + f"{operacion_numero}" + " realizada por calculadora_erre en esta sesion")
    num1 = float(input("\nIngresa un numero: "))
    op = input("\nIngresa un operador: ")
    num2 = float(input("\nIngresa otro numero: "))
    if op == "+":
        res = (num1 + num2)
        print()
        print("La suma es: " + str(res))
        op3 = input("\nIngresa [1] para realizar otra operacion o [2] para salir de calculadora_erre\n--> ")
        if op3 == "1":
            operacion_numero += 1
        elif op3 == "2":
            print("\nNos vemos en otra ocasión, gracias por usar la calculadora")
            input("\nPresiona ENTER para salir.")
            break

    elif op == "-":
        res = (num1 - num2)
        print()
        print("La resta es: " + str(res))
        op3 = input("\nIngresa [1] para realizar otra operacion o [2] para salir de calculadora_erre\n--> ")
        if op3 == "1":
            operacion_numero += 1
        elif op3 == "2":
            print("\nNos vemos en otra ocasión, gracias por usar la calculadora")
            input("\nPresiona ENTER para salir.")
            break

    elif op == "*":
        res = (num1 * num2)
        print()
        print("La multiplicacion es: " + str(res))
        op3 = input("\nIngresa [1] para realizar otra operacion o [2] para salir de calculadora_erre\n--> ")
        if op3 == "1":
            operacion_numero += 1
        elif op3 == "2":
            print("\nNos vemos en otra ocasión, gracias por usar la calculadora")
            input("\nPresiona ENTER para salir.")
            break

    elif op == "**":
        res = (num1 ** num2)
        print()
        print("La potencia es: " + str(res))
        op3 = input("\nIngresa [1] para realizar otra operacion o [2] para salir de calculadora_erre\n--> ")
        if op3 == "1":
            operacion_numero += 1
        elif op3 == "2":
            print("\nNos vemos en otra ocasión, gracias por usar la calculadora")
            input("\nPresiona ENTER para salir.")
            break

    elif op == "/":
        res = (num1 / num2)
        print()
        print("La division es: " + str(res))
        op3 = input("\nIngresa [1] para realizar otra operacion o [2] para salir de calculadora_erre\n--> ")
        if op3 == "1":
            operacion_numero += 1
        elif op3 == "2":
            print("\nNos vemos en otra ocasión, gracias por usar la calculadora")
            input("\nPresiona ENTER para salir.")
            break
    else:
        print("\nEl operador que ingresaste es invalido \nLos operadores validos son +, -, *, **, /\n")
