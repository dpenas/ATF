from random import randint
def randomoneorzero(length):
	aux = ""
	for i in range(length):
		aux = aux + str(randint(0,1))
	return aux

def sum_words (a, b, length):

	result = list(randomoneorzero(length))
	check = 0
	for i in range(len(a)-1, -1, -1):
		if ((a[i] == "0") and (b[i] == "0")):
			result[i] = "0"
			if (check):
				result[i] = "1"
				check = 0
		elif (((a[i] == "1") and (b[i] == "0")) or ((a[i] == "0") and (b[i] == "1"))):
			result[i] = "1"
			if (check):
				result[i] = "0"
				check = 1
		else:
			result[i] = "0"
			if (check):
				result[i] = "1"
			check = 1
	return "".join(result)

def codify(a, b, c, d):
	basenumber = randomoneorzero(len(a)*2) 
	right = sum_words(a, c, len(c))
	left = sum_words(b, d, len(a))
	final = left + right
	print final
	realfinal = sum_words(basenumber, final, len(basenumber))
	print realfinal
