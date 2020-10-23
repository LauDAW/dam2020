print("== ¿Qué edad vas a cumplir? ==")

anyo_actual = int(input("¿En qué año estamos?: "))

personas = []


for i in range(3):
    nombre = input("Introduce un nombre: ")
    anyo_nacimiento = int(input("Introduce un año de nacimiento: "))

    if anyo_nacimiento > anyo_actual:
        print("No puede ser un año de nacimiento mayor a la fecha actual.")
    else:
        print(nombre, "cumple ", (anyo_actual - anyo_nacimiento), "en el año", anyo_actual)
