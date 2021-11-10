# En todos los casos lo importante es realizar un diseño que cumpla con los
# criterios de calidad, mantenibilidad y testeabilidad del mismo.
# El foco esta en el diseño de la solución del problema y no en el código 
# específicamente. La solución puede describirse como resulté más claro ya sea 
# con código, pseudo código, con diagramas o como se crea más conveniente.

# Billetes

# Dado una suma en pesos sin centavos es necesario determinar cuál es la forma 
# de pagar dicha suma si se cuenta con  una cantidad determinada de billetes de 
# cada denominación en la caja.
# Los billetes pueden ser de: 100, 50, 20, 10, 5 y 1 pesos.
# Se arranca con una cantidad dada de billetes de cada denominación y se debe 
# determinar qué billetes se deben entregar para pagar la suma especificada.
# Es deseable que la cantidad de billetes sea la mínima posible no siendo 
# necesario que sea así en todos los casos estrictamente.
# Por ejemplo:
# si tengo 2 billetes de 100, 1 de 50 y 3 de 10
# y la suma a pagar es de 70
# el resultado es de 1 billete de 50 y 2 billetes de 10.

from timeit import default_timer as timer

# initialize a cash dictionary, the keys are the value of the bills,
# the items the quantity of the corresponding bill
# inputs: int, indicating the available bills.
def set_cash_bills(cien=0, cincuenta=0, veinte=0, diez=0, cinco=0, un=0):
	cash_dict = {100:cien, 50:cincuenta, 20:veinte, 10:diez, 5:cinco, 1:un}

	return cash_dict

# returns a cash dict, with the quantity of used bills to pay the amount
# indicated by receipt
# cash_dict: cash dict, receipt: int
def greedy_pay(cash_dict, receipt):
	owed = receipt
	n_used_bills = 0
	used_cash = set_cash_bills()

	for bill_value, bills_owned in cash_dict.items():
		if bills_owned and (bill_value < owed):
			n_used_bills = owed//(bill_value)
			owed = owed - bill_value*n_used_bills

			used_cash[bill_value] = n_used_bills
		n_used_bills = 0
	
	return used_cash

# Shows the used bills.
def print_used(used_cash):
	print("Billetes usados:")
	for bill_value, bills_used in used_cash.items():
		if bills_used !=0:
			print ("{} de {}".format(bills_used, bill_value))


# Initialize the cash available, 2 billetes de 100, 1 de 50 y 3 de 10.
cash = set_cash_bills(2,1,0,3,0,0)
total_pay = 70
# Initialize the cash dict to zero
used_cash = set_cash_bills()

# start = timer()
used_cash = greedy_pay(cash, total_pay)
# end = timer()
# print(end - start)

print_used(used_cash)