import multiprocessing
import os
import math

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
    mylist = [2, 4, 9, 16, 25, 36, 125, 64, 81, 100]

    p1 = multiprocessing.Process(target=raizcuadrada, args=(mylist,))
    p2 = multiprocessing.Process(target=raizcuadrada, args=(mylist,))

    p1.start()
    p2.start()

    print('> ID del proceso principal: {}'.format(os.getpid()))
    print('> ID del p1: {}'.format(p1.pid))
    print('> ID del p2: {}'.format(p2.pid))

    p1.join()
    p2.join()

    print('> Resultado en proceso main: {}'.format(raizcuadrada(result)))
    print("> Acabado.")

    print('> ¿El p1 está vivo? {}'.format(p1.is_alive()))
    print('> ¿El p2 está vivo? {}'.format(p2.is_alive()))
