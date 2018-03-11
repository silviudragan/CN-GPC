from pprint import pprint
from operator import itemgetter

global matrice_a
global vector_a
global dimensiune_a

global matrice_b
global vector_b
global dimensiune_b

global aplusb
global vector_rez
global dimensiune_rez


def citire_date():
    ###########################################################################
    ########################### Citire din a.txt ##############################
    ###########################################################################
    global matrice_a
    global vector_a
    global dimensiune_a
    matrice_a = []
    vector_a = []
    f = open("a.txt", 'r')
    dimensiune_a = int(f.readline())
    nimic = f.readline()

    it = dimensiune_a
    while it:
        vector_a.append(float(f.readline()))
        it -= 1
        matrice_a.append([])

    nimic = f.readline()
    length = 3
    while length != 1:
        try:
            line = f.readline()[:-1].split(', ')
            int_line = [float(i) for i in line]
            length = len(line)
            valoare = []

            if int_line[2] - int(int_line[2]) == 0:
                int_line[2] = int(int_line[2])

            if int_line[0] - int(int_line[0]) == 0:
                int_line[0] = int(int_line[0])

            valoare.append(int_line[0])
            valoare.append(int_line[2])
            matrice_a[int(int_line[1])].append(valoare)
        except Exception:
            length = 1

    # pprint(matrice_a)


    ###########################################################################
    ########################### Citire din b.txt ##############################
    ###########################################################################
    global matrice_b
    global vector_b
    global dimensiune_b
    matrice_b = []
    vector_b = []
    f = open("b.txt", 'r')
    dimensiune_b = int(f.readline())
    nimic = f.readline()

    it = dimensiune_b
    while it:
        vector_b.append(float(f.readline()))
        it -= 1
        matrice_b.append([])

    nimic = f.readline()
    length = 3
    while length != 1:
        try:
            line = f.readline()[:-1].split(', ')
            int_line = [float(i) for i in line]
            length = len(line)
            valoare = []

            if int_line[2] - int(int_line[2]) == 0:
                int_line[2] = int(int_line[2])

            if int_line[0] - int(int_line[0]) == 0:
                int_line[0] = int(int_line[0])

            valoare.append(int_line[0])
            valoare.append(int_line[2])
            matrice_b[int(int_line[1])].append(valoare)
        except Exception:
            length = 1
            # pprint(matrice_b)


def adunare():
    aplusb = []
    for i in range(dimensiune_a):
        line = []
        aplusb.append(line)

    for i in range(dimensiune_a):
        for j in range(dimensiune_a):
            el_a = None
            el_b = None
            for item in matrice_a[i]:
                if item[1] == j:
                    el_a = item[0]
            for item in matrice_b[i]:
                if item[1] == j:
                    el_b = item[0]

            # print(i, j, el_a, el_b)
            if el_a is not None and el_b is not None:
                valoare = []
                valoare.append(el_a + el_b)
                valoare.append(j)
                try:
                    aplusb[i].append(valoare)
                except Exception:
                    pass
            elif el_a is not None:
                valoare = []
                valoare.append(el_a)
                valoare.append(j)
                # print(i, j, valoare)
                try:
                    aplusb[i].append(valoare)
                except Exception:
                    pass
            elif el_b is not None:
                valoare = []
                valoare.append(el_b)
                valoare.append(j)
                try:
                    aplusb[i].append(valoare)
                except Exception:
                    pass

    for i in range(dimensiune_a):
        for j in range(dimensiune_a):
            try:
                if aplusb[i][j][0] - int(aplusb[i][j][0]) == 0:
                    aplusb[i][j][0] = int(aplusb[i][j][0])
            except Exception:
                pass
    return aplusb


def citire_rezultat():
    global aplusb
    global vector_rez
    global dimensiune_rez

    aplusb = []
    vector_rez = []
    f = open('aplusb.txt', 'r')
    dimensiune_rez = int(f.readline())
    nimic = f.readline()

    it = dimensiune_rez
    while it:
        vector_rez.append(float(f.readline()))
        it -= 1
        aplusb.append([])

    nimic = f.readline()
    length = 3
    while length != 1:
        try:
            line = f.readline()[:-1].split(', ')
            int_line = [float(i) for i in line]
            length = len(line)
            valoare = []

            if int_line[2] - int(int_line[2]) == 0:
                int_line[2] = int(int_line[2])

            if int_line[0] - int(int_line[0]) == 0:
                int_line[0] = int(int_line[0])

            valoare.append(int_line[0])
            valoare.append(int_line[2])
            aplusb[int(int_line[1])].append(valoare)
        except Exception:
            length = 1
    for i in range(dimensiune_a):
        for j in range(dimensiune_a):
            try:
                if aplusb[i][j][0] - int(aplusb[i][j][0]) == 0:
                    aplusb[i][j][0] = int(aplusb[i][j][0])
            except Exception:
                pass

    return aplusb


def sortare(rez):
    for i in range(dimensiune_rez):
        rez[i] = sorted(rez[i], key=itemgetter(1))
    return rez


def main():
    citire_date()
    aplusb = adunare()
    rez = citire_rezultat()
    rez = sortare(rez)

    for i in range(dimensiune_rez):
        for j in range(dimensiune_rez):
            try:
                if aplusb[i][j] != rez[i][j]:
                    print(i, j, aplusb[i][j], rez[i][j])
                    break
            except Exception:
                pass
main()
