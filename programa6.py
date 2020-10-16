print("== Divisores de un número ==")

num = int(input("Introduzca un número entero (mayor que 0): "))

if num <= 0:
    print("Por favor, introduzca un número MAYOR que 0.")
else:
    for i in range(1, (num + 1)):
        if num % i == 0:
            print(i)