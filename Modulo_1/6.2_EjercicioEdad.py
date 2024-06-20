edad = float(input("Ingresa la edad de la persona:"))
if edad < 13:
    print ("La persona es un niño")
elif edad < 18:
    print ("La persona es un adolescente")
elif edad < 65:
    print ("La persona es un adulto")
else:
    print ("La persona es un adulto mayor")
