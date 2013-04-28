import math
import sys
from random import randint

def receiveinput():
	x = input("Enter the number of columns: ")
	y = input("Enter the number of rows: ")
	return (x,y)

def randommatrix(x1, y1, x2, y2):
	matrix1 = [[0 for _ in range(x1)] for _ in range(y1)]
	matrix2 = [[0 for _ in range(x2)] for _ in range(y2)]
	for number1 in range(x1):
		for number2 in range(y1):
			matrix1[number2][number1] = randint(0,10) # both inclusive
	for numbersecond1 in range(x2):
		for numbersecond2 in range(y2):
			matrix2[numbersecond2][numbersecond1] = randint(0,10) # both inclusive	
	print "First matrix: " + str(matrix1)
	print "Second matrix: " + str(matrix2)
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
	count1 = 0
	count2 = 0
	count3 = 0
	if (flag == 1):
		a = receiveinput()
		b = receiveinput()
		if (a[0] != b[1]):
			print("The rows and columns don't match. Please enter a correct matrix")
			exit(0)
		(matrix1, matrix2) = randommatrix(a[0], a[1], b[0], b[1])
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
		print "Here are the first values:"
		print matrix1
		print matrix2
		print i
		print j
		print k
		print mult
		print "Restarting the operation from this matrix: "
		print str(mult)
	r1 = len(matrix1)
	c1 = len(matrix1[0])
	r2 = len(matrix2)
	c2 = len(matrix2[0])
	print "r1: " + str(r1)
	print "c1: " + str(c1)
	print "r2: " + str(r2)
	print "c2: " + str(c2)
	if (flag == 1):
		mult = [[0 for _ in range(c2)] for _ in range(r1)]
	print mult
	for a in range(i,r1):
		count1 = count1 + 1
		for b in range(j, c2):
			for c in range(k, r2):
				mult[a][b] += matrix1[a][c] * matrix2[c][b]
				print "Valor de r1: \n" + str(r1)
				print "Valor de c1: \n" + str(c1)
				print "Valor de r2: \n" + str(r2)
				print "Valor de c2: \n" + str(c2)
				print "Valor de j: \n" + str(j)
				print "Valor de k: \n" + str(k)
				print "Valor de a: \n" + str(a)
				print "Valor de b: \n" + str(b)
				print "Valor de c: \n" + str(c)
				sys.stdin.read(1)
		printoutputfile(count1, 0, 0, mult)
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
	
