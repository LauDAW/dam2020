print("== Función filtrar_palabras() ==")

lista = []

num_palabras = int(input("Introduzca un número de palabras a introducir: "))

for i in range(num_palabras):
    print("Introduzca una palabra: ")
    palabra = input()
    lista += [palabra]

print("La lista de palabras generadas es :", lista)

n = int(input("Introduce un dígito para sacar las palabras con más letras que ese número: "))


def filtrar_palabras(lista, n):
    nueva_lista = []
    for i in lista:
        if len(i) > n:
            nueva_lista.append(i)
    return nueva_lista


print(filtrar_palabras(lista, n))
