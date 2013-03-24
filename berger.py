import math

def numberdigits(a):
	number_digits = len(a)
	print "Number digits: " + str(number_digits)
	num_final_bits = int(math.ceil(math.log(number_digits+1, 2)))
	print "Numero de digitos reales: " + str(num_final_bits)
	return num_final_bits

def number_zeros(a):
	count = 0
	for number in range(len(a)):
		if (a[number] == "1"):
			count = count + 1
	return count

def complement(a):
	b = ""
	for number in range(len(a)):
		if (a[number] == "0"):
			b = b + "1"
		else:
			b = b + "0"
	return b

def codify(a):
	num_bits = numberdigits(a)
	num_zeros = number_zeros(a)
	print num_zeros
	to_bin = lambda x: x >= 0 and str(bin(x))[2:]
	num_bin = to_bin(num_zeros)
	final_number = ""
	print num_bin
	if (num_zeros == 0):
		for i in range(num_bits):
			final_number += "0"
		final_number = complement(final_number)
		return final_number
	else:
		num_digits_result = int(math.log10(float(num_bin)))+1
	if (num_bits != num_digits_result):
		for i in range(abs(num_bits - num_digits_result)):
			final_number = final_number + "0"
	final_number = final_number + num_bin
	final_number = complement(final_number)
	return final_number

def decodify(a):

