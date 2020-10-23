print("== Función mas_larga() ==")

lista = ["patata", "cacatua", "albacete"]


def mas_larga(lista):
    larga = 0
    for i in lista:
        if len(i) > len(lista):
            larga = i
    return larga

print(mas_larga(lista))