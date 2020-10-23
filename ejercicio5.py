print("== Convertir números binarios en enteros ==")

binario = int(input("Introduce un número binario para transformar: "))

def binario_a_entero(binario):
    decimal = 0
    binario = str(binario)
    decimal = int(binario, 2)

    return decimal

print("El número binario", binario, "equivale a", binario_a_entero(binario))
