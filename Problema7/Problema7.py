from Mergesort import MergeSort


def Problema7(X, Y):
    peso_totale_x = sum(X)
    peso_totale_y = sum(Y)

    array_Y = []

    for y in range(len(Y)):
        array_Y.append((Y[y], y))

    MergeSort(array_Y, 0, len(array_Y) - 1)

    differenza_peso = abs(peso_totale_x - peso_totale_y)
    if differenza_peso % 2 != 0:
        return None

    for x in range(len(X)):
        y = BinSearch(array_Y, X[x], 0, len(array_Y) - 1, differenza_peso)
        if y != -1:
            return (x, y[1])
    return None


def BinSearch(a, x, i, j, differenza_peso):
    if i > j:
        return -1
    m = (i + j) // 2
    if abs(x - a[m][0]) == differenza_peso // 2:
        return a[m]
    if abs(x - a[m][0]) < differenza_peso // 2:
        return BinSearch(a, x, m + 1, j, differenza_peso)
    else:
        return BinSearch(a, x, i, m - 1, differenza_peso)


X = [0, 0, 0, 2, 0, 0, 0, 18, 0, 0, 0]
Y = [0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0]

print(Problema7(X, Y))
