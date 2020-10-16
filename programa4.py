print("== Introducir par y después impar ==")

par = int(input("Introduzca un número par (positivo o negativo): "))

if par % 2 == 0:
    impar = int(input("Introduzca un número impar (positivo o negativo): "))
    if impar % 2 == 1:
        print("Ha introducido los números correctamente, ¡enhorabuena!")
    elif impar % 2 == 0:
        print("Ha introducido un número incorrecto, inténtelo de nuevo.")
else:
    print("Ha introducido un número incorrecto, inténtelo de nuevo.")