"""
Ejercicio #2
Escribir un script que muestre por pantalla
todos los números pares del 1 al 120
"""

contador = 1

for contador in range (1, 121):
    if contador%2 == 0:
        print(f"{contador} es par")
    else:
        print(f"{contador} es impar")

