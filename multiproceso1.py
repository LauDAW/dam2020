import multiprocessing
import math
# import os

result = []
suma = 0


def raizcuadrada(mylist):
    global result
    global suma

    for i in mylist:
        result.append(round(math.sqrt(i)))

    suma = sum(result)

    print('Las raíces cuadradas de la lista son: {}'.format(result))
    print('La suma de las raíces cuadradas es: {}'.format(suma))

    return result


if __name__ == '__main__':
    # Si quisieramos ver el ID del main descomentar la línea de debajo y el "import os"
    # print('El ID del running main es: {}'.format(os.getpid()))

    mylist = [2, 4, 9, 16, 25, 36, 125, 64, 81, 100]

    p1 = multiprocessing.Process(target=raizcuadrada, args=(mylist,))

    p1.start()

    p1.join()

    print('Resultado en proceso main: {}'.format(raizcuadrada(result)))
    print("Acabado.")

    print('¿El p1 está vivo? {}'.format(p1.is_alive()))
