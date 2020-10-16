print("== Lista de palabras ==")
lista = []

num_palabras = int(input("Introduzca un número de palabras a introducir: "))

for i in range(num_palabras):
    print("Introduzca una palabra: ")
    palabra = input()
    lista += [palabra]

print("La lista de palabras generadas es :", lista)