print("== Implementar programa 5 en funciones ==")

num_min = int(input("Introduzca el número mínimo: "))
num_max = int(input("Introduzca el número máximo: "))

def paroimpar(num_min, num_max):
    for i in range(num_min, (num_max + 1)):
        if i % 2 == 0:
            print(f"{i} es par.")
        else:
            print(f"{i} es impar.")

if num_min > num_max:
    print("Número máximo y mínimo introducidos al revés. Pruebe de nuevo.")
    print("Ejemplo: número mínimo 5 y número máximo 27")
else:
    paroimpar(num_min, num_max)

print("== Implementar programa 6 en funciones ==")

num = int(input("Introduzca un número entero (mayor que 0): "))

def divisores(num):
    for i in range(1, (num + 1)):
        if num % i == 0:
            print(i)

if num <= 0:
    print("Por favor, introduzca un número MAYOR que 0.")
else:
    divisores(num)
