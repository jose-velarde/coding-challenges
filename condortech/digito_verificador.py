# En todos los casos lo importante es realizar un diseño que cumpla con los
# criterios de calidad, mantenibilidad y testeabilidad del mismo.
# El foco esta en el diseño de la solución del problema y no en el código 
# específicamente. La solución puede describirse como resulté más claro ya sea 
# con código, pseudo código, con diagramas o como se crea más conveniente.

# Dígito Verificador
# Para calcular el dígito verificador, se deben realizar los siguientes pasos:
# A. Invertir el número. (e.g: de 201012341 a 143210102).
# B. Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se 
# acaban los números, se debe comenzar de nuevo, por ejemplo, con 143210102:
# 1*2+4*3+3*4+2*5+1*6+0*7+1*2+0*3+2*4=52
# C. Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:
# 52 % 11 = 8
# Con el resultado obtenido en el paso anterior, debemos restarlo de 11:
# 11 - 8 = 3
# D. Si el resultado es 11 entonces se intercambia por 0, si es 10 es 1.

from itertools import cycle
from timeit import default_timer as timer

# returns a list with each digit (int) of input_number in reverse order 
# input_number: int
def split_and_reverse(input_number):
	digit_list = []
	
	while input_number:
		digit_list.append(input_number % 10)
		input_number = input_number // 10
	# print(digit_list)
	return digit_list 

# returns the sequence list with additional items to match the length of digit_list.
# if digit_list is shorter, the same sequence is returned
# digit_list: list of int, sequence: list of int
def extend_sequence(digit_list, sequence):
	sequence_ext = sequence.copy()
	n_over = len(digit_list) - len(sequence_ext)

	if not n_over <= 0:
		for over, seq_item in zip(range(n_over), sequence):
			sequence_ext.append(seq_item)
	# print(sequence_ext)
	return sequence_ext

# returns the check digit
# input: int, sequence: list of int
def check_digit(input, sequence):
	sum = 0
	dig_list = split_and_reverse(input)
	seq_list = extend_sequence(dig_list, sequence)
	
	for input_dig, seq_dig in zip(dig_list, seq_list):
		sum += int(input_dig) * seq_dig
	
	result = 11 - sum % 11
	
	if result == 11:
		result = 0
		return result
	elif result == 10:
		result = 1
		return result
	else:
		return result

# # returns the check digit, loops over the input by casting to string and manipulating the string.
# # input: int, sequence: list of int
# def check_digit_cast(input, sequence):
# 	sum = 0

# 	for input_dig, seq_dig in zip(reversed(str(input)),cycle(sequence)):
# 		sum += int(input_dig) * seq_dig
	
# 	result = 11 - sum % 11
	
# 	if result == 11:
# 		result = 0
# 		return result
# 	elif result == 10:
# 		result = 1
# 		return result
# 	else:
# 		return result

# input data
seq = [2,3,4,5,6,7]
input_num = 201012341

# basic functions version benchmark
start = timer()
control_digit = check_digit(input_num, seq)
end = timer()
print(end - start)

# # string manipulation version benchmark
# start = timer()
# control_digit = check_digit_cast(input_num, seq)
# end = timer()
# print(end - start)

print(control_digit)