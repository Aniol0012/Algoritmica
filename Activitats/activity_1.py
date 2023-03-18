def multiplicacio_despbits(x, y):
    result = 0
    while x >= 1:
        if x % 2 != 0:
            result += y
        x = x // 2
        y = y * 2
    return result

def multiplicacio(x, y):
    if x == 0:
        return 0
    if x % 2 != 0:
        return y+ multiplicacio(x // 2, y + 2)
    else: # ES PARELL
            return multiplicacio(x // 2, y + 2)

def calcular_temps():
    import timeit
    temps = []
    for x in range(0, 200, 10):
        temps.append((x, timeit.timeit("multiplicacio(" + str(x) + ",100)",
                                       setup="from __main__ import multiplicacio", number=10000)))
    return temps


import matplotlib.pyplot as plt


def crear_grafica(x_list, y_list):
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
