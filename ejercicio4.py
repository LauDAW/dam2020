print("== ¿Cuántas letras mayúsculas tiene? ==")

cadena = input("Introduce una frase: ")

def cuantas_mayus(cadena):
    cont = 0
    for i in cadena:
        if i != i.lower():
            cont = cont + 1
    return cont

print(f"{cadena} tiene {cuantas_mayus(cadena)} letras mayúsculas.")
