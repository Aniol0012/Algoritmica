#!/usr/bin/python3

def sorting(seq):  # Iterativa
    n = len(seq)
    for i in range(n):
        for j in range(n - i - 1, ):  # li restem 1 perq no fa falta anar fins al final
            if seq[i] > seq[j + 1]:  # Si l'anterior és mes gran que l'anterior, fem el swap
                seq[j], seq[j + 1] = seq[j + 1], seq[j]  # La coma fa el swap
    return seq

# Desordenat: O(n^2)
# Ordenat: O(n^2)
# Revès: O(n^2)


def random_list(length):
    # Random integer list generator
    import random
    new_list = list(range(length))
    random.shuffle(new_list)
    return new_list


def calcular_temps(times):
    import timeit
    temps = []
    for x in range(0, 1000, 10):
        sequence = random_list(x)
        temps.append((x, timeit.timeit("sorting(random_list(" + str(x) + "))",
                                       setup="from __main__ import sorting, random_list", number=times)))
    return temps


def calcular_temps_sorted(times):
    import timeit
    temps = []
    for x in range(0, 1000, 10):
        temps.append((x, timeit.timeit("sorting(list(range(" + str(x) + ")))",
                                       setup="from __main__ import sorting, random_list", number=times)))
    return temps


def calcular_temps_reverse(times):
    import timeit
    temps = []
    for x in range(0, 1000, 10):
        temps.append((x, timeit.timeit("sorting(list(range(" + str(x) + ",-1,-1)))",
                                       setup="from __main__ import sorting, random_list", number=times)))
    return temps


def crear_grafica(temps, temps2, temps3):
    import matplotlib.pyplot as plt
    x_list, y_list = map(list, zip(*temps))
    x_list2, y_list2 = map(list, zip(*temps2))
    x_list3, y_list3 = map(list, zip(*temps3))

    plt.scatter(x_list, y_list, color=['red'])
    plt.scatter(x_list2, y_list2, color=['blue'])
    plt.scatter(x_list3, y_list3, color=['green'])

    plt.show()


if __name__ == '__main__':
    temps = calcular_temps(1)
    temps_sorted = calcular_temps_sorted(1)
    temps_reversed = calcular_temps_reverse(1)
    crear_grafica(temps, temps_sorted, temps_reversed)
