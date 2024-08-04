# Problema:
# Escriba un programa que procese una lista de estudiantes con sus respectivas calificaciones en diferentes materias,
# calcule el promedio de cada estudiante y luego ordene a los estudiantes por su promedio en orden descendente.

# Instrucciones:
# 1. Defina una lista de diccionarios, donde cada diccionario representa un estudiante y contiene su nombre y sus calificaciones en diferentes materias.
<<<<<<< HEAD
=======
# 2. Calcule el promedio de calificaciones de cada estudiante.
# 3. Añada el promedio al diccionario de cada estudiante.
# 4. Ordene la lista de estudiantes por el promedio en orden descendente.
# 5. Imprima la lista ordenada de estudiantes con sus promedios.

# Definir la lista de diccionarios con los estudiantes y sus calificaciones
>>>>>>> d4e3655012400de0e8a0d835eb9ba32d156d8eb5
estudiantes = [
    {"nombre": "Alice", "matematicas": 85, "literatura": 78, "ciencia": 92},
    {"nombre": "Bob", "matematicas": 89, "literatura": 94, "ciencia": 85},
    {"nombre": "Charlie", "matematicas": 72, "literatura": 67, "ciencia": 80},
    {"nombre": "David", "matematicas": 90, "literatura": 88, "ciencia": 91},
    {"nombre": "Eva", "matematicas": 88, "literatura": 76, "ciencia": 85}
]
<<<<<<< HEAD
# 2. Calcule el promedio de calificaciones de cada estudiante.
=======
>>>>>>> d4e3655012400de0e8a0d835eb9ba32d156d8eb5

for estudiante in estudiantes:
    calificaciones = [i for i in estudiante.values() if type(i) == int ]
    promedio = sum(calificaciones) / len(calificaciones)

<<<<<<< HEAD
# 3. Añada el promedio al diccionario de cada estudiante.
    estudiante["promedio"] = promedio

# 4. Ordene la lista de estudiantes por el promedio en orden descendente.
orden = sorted(estudiantes, key = lambda x:x["promedio"],reverse=True)

# 5. Imprima la lista ordenada de estudiantes con sus promedios.
for estudiante in orden:
=======
    #estudiante["matematicas"] + estudiante["literatura"] + estudiante["ciencia"]
    #promedio = suma_total / 3
    estudiante["promedio"] = promedio

for estudiante in estudiantes:
>>>>>>> d4e3655012400de0e8a0d835eb9ba32d156d8eb5
    print(f'{estudiante["nombre"]} - Promedio: {estudiante["promedio"]:.2f}')