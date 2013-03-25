def sum_wordsleft (a, c):
	result = list("0000")
	check = 0
	for i in range(len(a)-1, -1, -1):
		if ((a[i] == "0") and (c[i] == "0")):
			result[i] = "0"
			if (check):
				result[i] = "1"
				check = 0
		elif (((a[i] == "1") and (c[i] == "0")) or ((a[i] == "0") and (c[i] == "1"))):
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
def sum_wordsright (b, d):
	result = list("0000")
	check = 0
	for i in range(len(b)-1, -1, -1):
		if ((b[i] == "0") and (d[i] == "0")):
			result[i] = "0"
			if (check):
				result[i] = "1"
				check = 0
		elif (((b[i] == "1") and (d[i] == "0")) or ((b[i] == "0") and (d[i] == "1"))):
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
	left = sum_wordsleft(a,c)
	right = sum_wordsright(b,d)
	final = left + right
	return final
