import math
import sys
from random import randint

def receiveinput():
	x = input("Enter the number of columns: ")
	y = input("Enter the number of rows: ")
	return (x,y)

def randommatrix(x, y):
	matrix1 = [[0 for _ in range(x)] for _ in range(y)]
	matrix2 = [[0 for _ in range(x)] for _ in range(y)]

	for number1 in range(x):
		for number2 in range(y):
			matrix1[number2][number1] = randint(0,10) # both inclusive
			matrix2[number2][number1] = randint(0,10) # both inclusive
	return (matrix1, matrix2)

def multiply():
	a = receiveinput()
	(matrix1, matrix2) = randommatrix(a[0], a[1])
	r1 = len(matrix1)
	c1 = len(matrix1[0])
	r2 = len(matrix2)
	c2 = len(matrix2[0])
	mult = [[0 for _ in range(c1)] for _ in range(r2)]
	for i in range(r1):
		for j in range(c2):
			for k in range(r2):
				mult[i][j] += matrix1[i][k] * matrix2[k][j]
	return mult
		

def main():
	multmat = multiply()
	return multmat
	
