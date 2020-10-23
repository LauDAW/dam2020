print("== Cuenta vocales ==")

frase = input("Elige una frase: ")
frase = frase.lower()
vocales = "aeiou"


def cuenta_vocales(frase, vocales):
    cont = 0
    for i in vocales:
        for j in frase:
            if j == i:
                cont = cont + 1
    return cont


print("La frase '", frase, "' tiene", cuenta_vocales(frase, vocales), "vocales")
