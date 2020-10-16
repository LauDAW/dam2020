print("== ¿Par o impar? ==")

num_min = int(input("Introduzca el número mínimo: "))
num_max = int(input("Introduzca el número máximo: "))

if num_min > num_max:
    print("Número máximo y mínimo introducidos al revés. Pruebe de nuevo.")
    print("Ejemplo: número mínimo 5 y número máximo 27")
else:
    for i in range(num_min, (num_max + 1)):
        if i % 2 == 0:
            print(f"{i} es par.")
        else:
            print(f"{i} es impar.")
