from pprint import pprint
import numpy as np
def ex1():
	number = 1
	precision = 0
	while number+1 != 1:
		precision += 1
		number /= 10

	return(1/pow(10,precision))

#print("Precizia masina este: ", ex1())

def ex2():
	x = 1.0
	y = ex1()
	z = ex1()
	x2 = 1.1
	#print("Adunare si Inmultire:")
	# de pus text si aici
	return (x+y)+z != x+(y+z), (x2*y)*z != x2*(y*z)

#print(ex2())
def putere_optima(n):
	i = 0
	while pow(2, i) < n:
		i += 1
	return pow(2, i), i

#print(putere_optima(5))

def matrixMul(m1, m2):
	m3 = []
	for i in range(0, len(m1)):
		line = []
		for j in range(0, len(m2)):
			sum = 0
			for k in range(0, len(m2)):
				sum += m1[i][k]*m2[k][j]
			line.append(sum)
		m3.append(line)
	return m3


def initialize_matrix(len):
    matrix = []
    line = []
    for i in range (len):
        for j in range (len):
            line.append(0)
        matrix.append(line)
        line = []
    return matrix


def matrixSum(m1,m2):
    rez = initialize_matrix(len(m1))
    for i in range(len(m1)):
        for j in range(len(m1)):
            rez[i][j] = m1[i][j] + m2[i][j]
    return rez


def matrixDiff(m1,m2):
    rez = initialize_matrix(len(m1))
    for i in range(len(m1)):
        for j in range(len(m1)):
            rez[i][j] = m1[i][j] - m2[i][j]
    return rez


def citire_date():
    f = open("input.txt", 'r')
    d = f.readline()
    n = f.readline()
    matrix1 = []
    matrix2 = []
    it = int(n)
    while it:
        line = f.readline().split()
        int_line = [int(i) for i in line]
        matrix1.append(int_line)
        it -= 1

    it = int(n)
    while it:
        line = f.readline().split()
        int_line = [int(i) for i in line]
        matrix2.append(int_line)
        it -= 1

    # popularea matricilor cu valori de 0 pentru a avea dimensiune ^2
    n = int(n)
    q, putere = putere_optima(n)
    if q != n:
        line_0 = [0 for i in range(0, q)]
        for i in range(0, q-n):
            for j in range(0, n):
                matrix1[j].append(0)
                matrix2[j].append(0)
            matrix1.append(line_0)
            matrix2.append(line_0)
    return matrix1, matrix2, putere, d


def multiply_Strassen(m1,m2,q,d):
    if int(q)>int(d):
        n1=pow(2,q-1)
        a11 = initialize_matrix(n1)
        a12 = initialize_matrix(n1)
        a21 = initialize_matrix(n1)
        a22 = initialize_matrix(n1)
        b11 = initialize_matrix(n1)
        b12 = initialize_matrix(n1)
        b21 = initialize_matrix(n1)
        b22 = initialize_matrix(n1)
        c11 = initialize_matrix(n1)
        c12 = initialize_matrix(n1)
        c21 = initialize_matrix(n1)
        c22 = initialize_matrix(n1)
        p1 = initialize_matrix(n1)
        p2 = initialize_matrix(n1)
        p3 = initialize_matrix(n1)
        p4 = initialize_matrix(n1)
        p5 = initialize_matrix(n1)
        p6 = initialize_matrix(n1)
        p7 = initialize_matrix(n1)
        for i in range(n1):
            for j in range(n1):
                a11[i][j] = m1[i][j]
                b11[i][j] = m2[i][j]
                a12[i][j] = m1[i][j+n1]
                b12[i][j] = m2[i][j+n1]
                a21[i][j] = m1[i+n1][j]
                b21[i][j] = m2[i+n1][j]
                a22[i][j] = m1[i+n1][j+n1]
                b22[i][j] = m2[i+n1][j+n1]
        p1 = multiply_Strassen(matrixSum(a11,a22),matrixSum(b11,b22),q-1,d)
        p2 = multiply_Strassen(matrixSum(a21,a22),b11,q - 1,d)
        p3 = multiply_Strassen(a11, matrixDiff(b12, b22), q - 1, d)
        p4 = multiply_Strassen(a22, matrixDiff(b21, b11), q - 1, d)
        p5 = multiply_Strassen(matrixSum(a11, a12),b22, q - 1, d)
        p6 = multiply_Strassen(matrixDiff(a21, a11), matrixSum(b11, b12), q - 1, d)
        p7 = multiply_Strassen(matrixDiff(a12, a22), matrixSum(b21, b22), q - 1, d)

        c11 = matrixSum(matrixDiff(matrixSum(p1,p4),p5  ),p7)
        c12 = matrixSum(p3,p5)
        c21 = matrixSum(p2,p4)
        c22 = matrixSum(matrixDiff(matrixSum(p1,p3),p2),p6)
        rez = []
        for i in range(n1):
            rez.append(c11[i]+c12[i])
        for i in range(n1):
            rez.append(c21[i]+c22[i])
        return rez
    else:
        return np.dot(m1,m2)


def ex3():
    m1,m2,q,d = citire_date()
    #pprint(np.dot(m1, m2))
    c=multiply_Strassen(m1,m2,q,d)
    return c
#pprint(ex3())

from tkinter import *


class GUI(object):
    def __init__(self, interfata):
        self.root = interfata

        self.text = Frame(self.root, width=1000, height=1000)
        self.text.pack(fill="both", expand=True)
        button = Button(self.text,text="Ex. 1", command = self.retrieve_input)
        button.grid(column=0,row=2)
        button2 = Button(self.text, text="Ex. 2", command=self.retrieve_input2)
        button2.grid(column=0, row=4)
        button3 = Button(self.text, text="Ex. 3", command=self.retrieve_input3)
        button3.grid(column=0, row=6)

    def retrieve_input(self):
        content = "Precizia masina este " + str(ex1())
        label = Label(self.text,text=content)
        label.grid(column=1,row=2)

    def retrieve_input2(self):
        rez = ex2()
        adunare = "asociativa"
        inmultirea = "asociativa"
        if rez[0]:
            adunare = "neasociativa"
        if rez[1]:
            inmultirea = "neasociativa"
        content = "Adunarea este " + adunare + " si inmultirea este " + inmultirea
        label = Label(self.text,text=content)
        label.grid(column=1,row=4)

    def retrieve_input3(self):
        rez = ex3()
        content = "Rezultatul inmultirii este: "
        label = Label(self.text, text=content)
        label.grid(column=1, row=6)
        for i in range(0, len(rez)):
            content = rez[i]
            label = Label(self.text,text=content)
            label.grid(column=1, row=7+i)
interfata = Tk()
app = GUI(interfata)
interfata.mainloop()
