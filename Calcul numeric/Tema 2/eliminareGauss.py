from math import fabs, sqrt
from pprint import pprint
import copy
import numpy as np

global dimensiune
global matrix
global precizie
global rezultat


def citire_date():
    global matrix
    global precizie
    global rezultat
    global dimensiune
    f = open("input.txt", 'r')
    dimensiune = f.readline()
    precizie = f.readline()
    dimensiune = int(dimensiune)
    precizie = 1 / pow(10, int(precizie))
    matrix = []
    it = dimensiune
    while it:
        line = f.readline().split()
        int_line = [int(i) for i in line]
        matrix.append(int_line)
        it -= 1
    # pprint(matrix1)
    rezultat = [int(i) for i in f.readline().split()]
    # print(rezultat)


citire_date()


def pivot(extinsa, l):
    max = fabs(extinsa[l][0])
    index = 0
    for i in range(1, dimensiune):
        if max < fabs(extinsa[i][l]):
            max = fabs(extinsa[i][l])
            index = i
    return index


def max_coloana(extinsa, coloana):
    max = fabs(extinsa[0][coloana])
    index = 0
    for i in range(1, dimensiune):
        if max < fabs(extinsa[i][coloana]):
            max = fabs(extinsa[i][coloana])
            index = i
    return index


def rezolva_sistem_superior_triunghiular(extinsa):
    solution = []
    for i in range(dimensiune - 1, -1, -1):
        it_solution = 0
        x = 0
        for j in range(dimensiune - 1, i, -1):
            x += solution[it_solution] * extinsa[i][j]
            it_solution += 1
        solution.append((extinsa[i][dimensiune] - x) / extinsa[i][i])
    rez = dict()
    for i in reversed(range(1, dimensiune + 1)):
        key = 'x' + str(dimensiune-i+1)
        rez[key] = solution[i - 1]
    return rez, list(reversed(solution))


def substitutie_inversa():
    extinsa = copy.deepcopy(matrix)
    for i in range(dimensiune):
        extinsa[i].append(rezultat[i])

    l = 0
    index_pivot = pivot(extinsa, l)
    au = extinsa[index_pivot][l]

    # interschimbarea celor 2 linii, daca este nevoie
    extinsa[index_pivot], extinsa[l] = extinsa[l], extinsa[index_pivot]
    while l < dimensiune - 1 and fabs(au) > precizie:
        for i in range(l + 1, dimensiune):
            f = extinsa[i][l] / extinsa[l][l]
            for j in range(l + 1, dimensiune + 1):
                extinsa[i][j] = extinsa[i][j] - f * extinsa[l][j]
            extinsa[i][l] = 0
        l += 1
        index_pivot = pivot(extinsa, l)

        # interschimbarea celor 2 linii, daca este nevoie
        extinsa[index_pivot], extinsa[l] = extinsa[l], extinsa[index_pivot]
        au = 0 - fabs(extinsa[l][l])
    if fabs(au) <= precizie:
        print("matrice singulara")
    else:
        solution, raw = rezolva_sistem_superior_triunghiular(extinsa)
        print("Solutia sistemului este ", solution)

        ##################################################################
        ##################### Verificare solutie #########################
        ##################################################################
        verificare_sol = np.dot(matrix, raw) - rezultat
        print("Verificarea solutiei ", verificare_sol)
        sum = 0
        for i in verificare_sol:
            sum += pow(fabs(i), 2)
        print("|| z || = ", sqrt(sum))
        # pprint(extinsa)


substitutie_inversa()
