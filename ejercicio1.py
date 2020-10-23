print("== Función max_in_list() ==")

lista_num = []

cuantos_num = int(input("¿Cuántos números quieres introducir? "))

for i in range(cuantos_num):
    num = int(input("Introduce un número: "))
    lista_num.append(num)


def max_in_list(lista_num):
    mayor = 0

    for i in lista_num:
        if mayor <= i:
            mayor = i
        else:
            mayor = mayor
    return mayor


print(f"El número mayor de {lista_num} es {max_in_list(lista_num)}")
