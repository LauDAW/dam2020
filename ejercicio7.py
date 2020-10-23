print("== Edades superiores a 20 ==")

tupla = []

print("Introduce edades de 10 personas")

for i in range(10):
    edad = int(input(f"Introduce edad de la persona {(i + 1)}: "))
    tupla.append(edad)

print(tupla)


def mas_de_20(tupla):
    cont = 0
    for i in tupla:
        if i > 20:
            cont = cont + 1
    return cont


print(f"Hay {mas_de_20(tupla)} personas con más de 20 años.")
