print("== Introducir par e impar ==")
par = int(input("Introduce un número par (positivo o negativo): "))
impar = int(input("Introduce un número impar (positivo o negativo): "))

if par % 2 == 1:
    print("En la sección par ha introducido un número incorrecto.")
    if impar % 2 == 0:
        print("En la sección impar ha introducido un número incorrecto.")
elif impar % 2 == 0:
    print("En la sección impar ha introducido un número incorrecto.")
    if par % 2 == 1:
        print("En la sección par ha introducido un número incorrecto.")
else:
    print("Ha introducido los números correctamente, ¡enhorabuena!")
