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
#	print "First matrix: " + str(matrix1)
#	print "Second matrix: " + str(matrix2)
	f = open('output.txt', 'w')
	f.write(str(matrix1))
	f.write("\n")
	f.write(str(matrix2))
	f.write("\n")
	f.close()
	return (matrix1, matrix2)

def printoutputfile(i, j, k, matrix):
	f = open('output.txt', 'r')
	line = f.readlines()
	line1 = line[0]
	f.close()
	f = open('output.txt', 'r')
	line2 = f.readlines()[1]
	f.close()
	f = open('output.txt', 'w')
	f.write(str(line1))
	f.write(str(line2))
	f.write(str(i) + "\n")
	f.write(str(j) + "\n")
	f.write(str(k) + "\n")
	f.write(str(matrix))
	f.close()

def readinformation():	
	f = open('output.txt', 'r')
	line = f.readlines()
	matrix1 = line[0]
	matrix2 = line[1]
	i = line[2]
	j = line[3]
	k = line[4]
	mul = line[5]
	return(matrix1,matrix2,i,j,k,mul)
def multiply(flag):
	if (flag == 1):
		a = receiveinput()
		(matrix1, matrix2) = randommatrix(a[0], a[1])
		print "Random matrix selected\n"
		i = 0
		j = 0
		k = 0
	else:
		a = readinformation()
		matrix1 = eval(a[0])
		matrix2 = eval(a[1])
		i = int(a[2])
		j = int(a[3])
		k = int(a[4])
		mult = eval(a[5])
		print "Restarting the operation from this matrix: "
		print str(mult)
	r1 = len(matrix1)
	c1 = len(matrix1[0])
	r2 = len(matrix2)
	c2 = len(matrix2[0])
	if (flag == 1):
		mult = [[0 for _ in range(c1)] for _ in range(r2)]
	for a in range(i,r1):
		for b in range(j, c2):
			for c in range(k, r2):
				mult[a][b] += matrix1[a][c] * matrix2[c][b]
		printoutputfile(a, b, c, mult)
	print "FINAL: " + str(mult)

def main():
	print "1.- Start a new operation\n"
	print "2.- Start from the checkpoint\n"
	foo = 0
	while (foo != 1 and foo != 2):
		foo = input("Please enter a value: ")
	if (foo == 1):
		multiply(1)
	else:
		multiply(2)
	
