print("== La búsqueda de la palabra ==")
lista = []

num_palabras = int(input("Introduzca un número de palabras a introducir: "))

for i in range(num_palabras):
    print("Introduzca una palabra: ")
    palabra = input()
    lista += [palabra]

print("La lista de palabras generadas es :", lista)

palabra_buscada = input("Introduzca la palabra a buscar: ")
num_veces = 0

for i in lista:
    if i == palabra_buscada:
        num_veces = num_veces + 1

if num_veces == 0:
    print("La palabra deseada no se encuentra en esta lista.")
else:
    print(f"La palabra {palabra_buscada} aparece en nuestra lista {num_veces} veces.")
