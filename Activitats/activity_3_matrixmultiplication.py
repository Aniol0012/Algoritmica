def matrixmultiplication(X, Y):
    result = []
    X_files = len(X)
    Y_files = len(Y)
    X_cols = len(X[0])
    Y_cols = len(Y[0])
    for i in range(X_files):
        result.append([]) # Afegeixo una fila
        result[i] = [0] * Y_cols # Afegim 0's
        for j in range(Y_cols):
            result[i][j] = 0 # Ptsr no fa falta
            for k in range(Y_cols):  # Operacio
                result[i][j] += X[i][k] * Y[k][j]

    return result


def random_matrix(n):
    """ Random integer matrix generator """
    import random
    X = []
    for i in range(n):
        X.append([])
        for j in range(n):
            X[i].append(random.randint(0, 100))
    return X


def calcular_temps():
    import timeit
    temps = []
    for x in range(1, 100, 10):
        matrix1 = random_matrix(x)
        matrix2 = random_matrix(x)
        temps.append((x, timeit.timeit("matrixmultiplication(" + str(matrix1) + "," + str(matrix2) + ")",
                                       setup="from __main__ import matrixmultiplication", number=100)))
    return temps


import matplotlib.pyplot as plt


def crear_grafica(x_list, y_list):
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
