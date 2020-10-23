print("== Nombres que empiezan por cierta letra ==")

nombres = []
num_nombres = int(input("¿Cuántos nombres quieres añadir?: "))

for i in range(num_nombres):
    actual = i + 1
    nombre = input(f"Elige el nombre número {actual}: ")
    nombres.append(nombre)

print(nombres)

letra = input("Elige letra para buscar cuántos empiezan por ella: ")

def cuenta_nombres(nombres, letra):
    cont = 0

    for i in nombres:
        if i[0] == letra.upper():
            cont = cont + 1
        elif i[0] == letra.lower():
            cont = cont + 1

    return cont

print(cuenta_nombres(nombres, letra))


