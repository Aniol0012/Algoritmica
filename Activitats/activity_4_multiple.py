def multiple3(number):
    #code
    return True

def sumdigits(number):
    #code
    return 0

def calcular_temps():
    import timeit
    temps = []
    for x in range(0, 200, 6):
        temps.append((x, timeit.timeit("multiple3(" + str(x) + ")",
                                       setup="from __main__ import multiple3", number=1000)))
    return temps


import matplotlib.pyplot as plt


def crear_grafica(x_list, y_list):
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
