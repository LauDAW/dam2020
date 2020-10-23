print("== ¿Es año bisiesto? ==")

anyo = int(input("Introduzca un año: "))


def es_bisiesto(anyo):
    if anyo % 4 == 0 and (not (anyo % 100 == 0)):
        print(f"{anyo} es un año bisiesto")
    else:
        print(f"{anyo} no es un año bisiesto")


es_bisiesto(anyo)
