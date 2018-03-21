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


def pivot(extinsa, l):
    max = fabs(extinsa[l][0])
    index = 0
    for i in range(l, dimensiune):
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
        try:
            solution.append((extinsa[i][dimensiune] - x) / extinsa[i][i])
        except Exception:
            pass
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
    print()
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
        print("|| z ||2 = ", sqrt(sum))
        # pprint(extinsa)



        sol_num = np.linalg.solve(matrix, rezultat)
        # print("linalg ", sol_num)
        ver_sol_num = np.dot(matrix, sol_num) - rezultat
        #print("ver sol num ", ver_sol_num)
        sum = 0
        for i in ver_sol_num:
            sum += pow(fabs(i), 2)
        print("Verificara solutiei cu ajutorul librariei:")
        print("|| A* Xgauss - b ||2 = ", sqrt(sum))


def main_mandatory():
    citire_date()
    substitutie_inversa()

main_mandatory()

global a
global b
global c


def citire_bonus():
    global a
    global b
    global c
    global precizie
    global rezultat
    global dimensiune
    f = open("input.txt", 'r')
    dimensiune = f.readline()
    precizie = f.readline()
    dimensiune = int(dimensiune)
    precizie = 1 / pow(10, int(precizie))
    a = []
    b = []
    c = []
    it = dimensiune
    pas = 0
    while it:
        line = f.readline().split()
        int_line = [int(i) for i in line]
        if pas != 0:
            c.append(int_line[pas-1])
        a.append(int_line[pas])
        try:
            b.append(int_line[pas+1])
        except Exception:
            pass
        pas += 1
        it -= 1
    rezultat = [int(i) for i in f.readline().split()]
    # print(a, b, c, rezultat)

global d
global e
global f

def inmultire_linie(x,i):
    if (c[i-1]):
        c[i-1] *= x
    a[i] *= x
    if len(b) > i:
        b[i] *= x
    if len(f) > i:
        f[i] *= x
    rezultat[i] *= x

def zero_sub_dig():
    global d
    global e
    global f
    d = []
    e = []
    f = []
    for i in range (0,dimensiune-2):
        f.append(0)
    for i in range(dimensiune-1):
        if fabs(c[i]) > fabs(a[i]):
            aux = a[i]
            a[i] = c[i]
            c[i] = aux
            aux = b[i]
            b[i] = a[i+1]
            a[i+1] = aux
            if len(b) > i + 1:
                aux = f[i]
                f[i] = b[i+1]
                b[i+1] = aux
            aux = rezultat[i]
            rezultat[i] = rezultat[i+1]
            rezultat[i+1] = aux
        aux = a[i]
        inmultire_linie(c[i], i)
        inmultire_linie(aux, i + 1)
        c[i] = 0
        a[i + 1] -= b[i]
        if len(b) > i + 1:
            b[i + 1] -= f[i]
        rezultat[i+1] -= rezultat[i]

    d = list(a)
    e = list(b)
    print(d,e,f,rezultat)



def rezolvare_sistem():
    solution = [int(0) for i in range(dimensiune)]
    solution[dimensiune-1] = rezultat[dimensiune-1]/d[dimensiune - 1]
    solution[dimensiune-2] = (rezultat[dimensiune-2] - e[dimensiune - 2]*solution[dimensiune-1])/d[dimensiune-2]
    pas = 0
    for i in range(dimensiune-3, -1, -1):
        x = dimensiune - pas - 1
        sum = 0
        sum += f[i]*solution[x]
        sum += e[i]*solution[x-1]
        sol = (rezultat[i] - sum)/d[i]
        pas += 1
        solution[i] = sol
    return solution


def main_bonus():
    citire_bonus()
    zero_sub_dig()
    solutie = rezolvare_sistem()
    print("Solutie bonus")
    print(solutie)


main_bonus()
