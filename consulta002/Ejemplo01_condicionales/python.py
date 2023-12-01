edad = int(input("Ingrese su edad por favor: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

nota = int(input("Ingrese su nota por favor: "))  

if nota == 20:
    print("Excelente")
elif nota >= 18:
    print("Bueno")
elif nota >= 16:
    print("Suficiente")
else:
    print("No has alcanzado la calificacion para aprobar")        