def sumofsquares(sequence):
    avg = sum(sequence) / len(sequence)
    s = 0
    for j in sequence:
        s += pow(j - avg, 2)
    return s


def sumofsquares_recursive(sequence, avg):
    if len(sequence) == 0:
        return 0
    else:
        return (sequence[0] - avg) ** 2 + sumofsquares_recursive(sequence[1:, avg])


def random_list(n):
    import random
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista


def calcular_temps():
    import timeit
    temps = []
    for x in range(1, 100, 10):
        sequence = random_list(x)
        temps.append((x, timeit.timeit("sumofsquares(" + str(sequence) + ")",
                                       setup="from __main__ import sumofsquares", number=10000)))
    return temps


import matplotlib.pyplot as plt


def crear_grafica(x_list, y_list):
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
