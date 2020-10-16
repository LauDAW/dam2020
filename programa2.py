print("== Calculadora de IMC ==")
peso = float(input("Introduce tu peso (kg): "))
altura = float(input("Introduce tu altura (m): "))

imc = (peso / (altura * altura))

print(f"Su imc es {imc}")
