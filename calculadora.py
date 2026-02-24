print("========Mi Super Calculadora==========")
num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

def suma(num_1, num_2):
    return num_1 + num_2

if operacion == "+":
    resultado = suma(num_1, num_2)
    print("El resultado de la suma es: ", resultado)

def res(num_1, num_2):
    return num_1 - num_2

if operacion == "-":
    resultado = res(num_1, num_2)
    print("El resultado de la resta es: ", resultado)

def mul(num_1, num_2):
    return num_1 * num_2

if operacion == "*":
    resultado = mul(num_1, num_2)
    print("El resultado de la multiplicacion es: ", resultado)

def div(num_1, num_2):
    return num_1 / num_2

if operacion == "/":
    resultado = div(num_1, num_2)
    print("El resultado de la suma es: ", resultado)