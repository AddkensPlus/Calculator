"""Calculadora"""

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

operacion = 0

while operacion != 6:
    print("""Que operacion deseas realizar?
          (1) Suma
          (2) Resta """)

    operacion = int(input())

    if operacion == 1:
        print("Suma: ", n1, "+", n2, "=", n1 + n2)
    elif operacion == 2:
        print("Resta: ", n1, "-", n2, "=", n1 - n2)
