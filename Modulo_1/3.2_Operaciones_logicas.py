
"""
Realiza un programa que solicite al usuario que introduzca tres números
luego realiza las siguientes verificaciones lógicas.

Paso 1: Solicitar tres números al usuario.
    Nota: Usa la función input() para pedir al usuario que introduzca tres números.
        La función float() se usa para convertir el valor introducido en un número decimal.
Paso 2: Verificar si los tres números son positivos.
Paso 3: Verificar si al menos uno de los números es negativo.
Paso 4: Verificar si el primer número es mayor que el segundo y el segundo es mayor que el tercero.
Paso 5: Mostrar los resultados.
    Nota: Usa la función print() para mostrar los resultados.
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

<<<<<<< HEAD
# ------------------------------------------------------------------
# En está sección agregar su codigo

## verificación si los 3 numeros son positivos
if num1 >= 0 and num2 >= 0 and num3 >= 0: 
    print("Los 3 numeros son positivos")
##validación si un numero es negativo
else :
    print("Uno de los numeros es negativo")
## Verificacion si el numero 1 es mayor que el numero 2 y el numero 2 que el numero 3
if num1>num2:
    print(f"El número {num1} es mayor que el número {num2}")
else:
    print(f"El número {num1} no es mayor que el número {num2}")
if num2>num3:
    print(f"El numero {num2} es mayor que el numero {num3}")
else:
    print(f"El numero {num2} no es mayor que el numero {num3}")
=======

# ------------------------------------------------------------------
# En está sección agregar su codigo

<<<<<<< HEAD
todos_positivos = 

al_menos_un_negativo = 

orden = 
# -------------------------------------------------------------------





=======
todos_positivos = num1>0 and num2>0 and num3>0

al_menos_un_negativo = num1<0 or num2<0 or num3<0

orden = num1>num2 and num2>3

# -------------------------------------------------------------------


>>>>>>> a91d3c6c82b0714aae9a78c17492bac0aa1eeeb7
print(f"Los tres números son positivos: {todos_positivos}")
print(f"Al menos uno de los números es negativo: {al_menos_un_negativo}")
print(f"El primero es mayor que el segundo y el segundo es mayor que el tercero: {orden}")
>>>>>>> d4e3655012400de0e8a0d835eb9ba32d156d8eb5
