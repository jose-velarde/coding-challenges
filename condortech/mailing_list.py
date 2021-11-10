# En todos los casos lo importante es realizar un diseño que cumpla con los
# criterios de calidad, mantenibilidad y testeabilidad del mismo.
# El foco esta en el diseño de la solución del problema y no en el código 
# específicamente. La solución puede describirse como resulté más claro ya sea 
# con código, pseudo código, con diagramas o como se crea más conveniente.

# Lista de Mails

# Se tiene una lista de mails que se obtienen de un mail server por IMAP. Cada 
# mail tiene asociado un string que representa una lista de flags separados 
# por espacio. 
# Se requiere diseñar una función donde se reciba la lista de mails y un string 
# que indique de qué manera se desea ordenar la lista. El string de orden se 
# especifica como una lista separada por | de los siguientes elementos: 
# [!]<FLAG>-(FIFO|LIFO) 
# Donde: 
# - el ! indica los elementos que no tengan el flag, de lo contrario son los 
# elementos que sí lo posean. 
# - FIFO y LIFO se refieren al orden que se desea para esos mails respecto de 
# su fecha de recepción. 
# La lista de orden indica la prioridad del FLAG para ser ordenado. Si un 
# elemento es ordenado por un criterio no debe repetirse ni volver a ordenarse por otro. 
#  
# Ejemplo: 
# MailA Flags: A B		Fecha de Recepción: 01/02/15 
# MailB Flags: A		Fecha de Recepción: 05/03/15 
# MailC Flags: B		Fecha de Recepción: 06/04/15 
# MailD Flags: A B		Fecha de Recepción: 08/09/15 
# MailE Flags: C		Fecha de Recepción: 07/11/15 
# MailF Flags: A C		Fecha de Recepción: 03/12/15 
#  
# Y si se especifica: B-LIFO|!C-FIFO|C-LIFO 
#  
# El orden a retornar es: 
# MailD Flags: A B		Fecha de Recepción: 08/09/15 
# MailC Flags: B		Fecha de Recepción: 06/04/15 
# MailA Flags: A B		Fecha de Recepción: 01/02/15 
# MailB Flags: A		Fecha de Recepción: 05/03/15 
# MailF Flags: A C		Fecha de Recepción: 03/12/15 
# MailE Flags: C		Fecha de Recepción: 07/11/15 

# mail object:
# identifier: mail designation.
# flags: string indicating the mail flags, i.e. "ABC"
# reception date: string indicating the reception date, i.e. "dd/mm/yy"
class Mail:
	def __init__(self, identifier, flags, reception_date):
		self.name = "Mail" + identifier	
		self.flags = flags
		self.reception_date = reception_date
		self.rec_date_int = self.convert_date(reception_date)
		self.flags_string = ""
		for character in flags:
			self.flags_string += character + " "
	
	# convert date string to int, "dd/mm/yy" -> yyyymmdd
	def convert_date(self, date):
		dd, mm, yy = date.split("/")
		return int("20{}{}{}".format(yy,mm,dd))

	# return the identifier when calling the object
	def __repr__(self):
		return self.name

	# return the mail information when printing to output
	def __str__(self):
		return "{} Flags: {:<8} Fecha de Recepción: {}".format(
			self.name, self.flags_string, self.reception_date)

def order_by_flag(mail_list, order_string):
	ordered_list = []
	temp_list = []
	# process the order string
	flag_string = order_string.split("|")
	for flag in flag_string:
		# get the flag ordering and date ordering req
		flag_id, date_order = flag.split("-")
		# print(flag_id, date_order)		

		# define the LIFO/FIFO ordering from the string
		if date_order == "LIFO":
			order_flag = True
		else:
			order_flag = False

		# iterate over every mail in the list, checking if mail has the indicated flag
		for mail in mail_list:
			# iterate just once per mail
			if mail not in ordered_list:
				# determine if the flag is an include or exclude flag
				if "!" not in flag_id:
					# append to temp_list if mail had the indicated flag
					if flag_id in mail.flags:
						temp_list.append(mail)
						# print(mail.name, "has flag", flag_id)
				else:
					if flag_id[1] not in mail.flags:
						# append to temp_list if mail does not have the indicated flag
						temp_list.append(mail)
						# print(mail.name, "does not have", flag_id)

		# print(temp_mail_list)

		# sort the temp_list by date, 
		# temp_list includes mails with/without flag_id. Add temp_list to the final list
		ordered_list += sorted(temp_list, key= lambda mail: mail.rec_date_int, reverse=order_flag)
		# initialize the temp_list
		temp_list = []

	return ordered_list

mail_A = Mail("A", "AB", "01/02/15")
mail_B = Mail("B", "A", "05/03/15")
mail_C = Mail("C", "B", "06/04/15")
mail_D = Mail("D", "AB", "08/09/15")
mail_E = Mail("E", "C", "07/11/15")
mail_F = Mail("F", "AC", "03/12/15")

mail_list = [mail_A, mail_B, mail_C, mail_D, mail_E, mail_F]

result_list = order_by_flag(mail_list, "B-LIFO|!C-FIFO|C-LIFO")

print(result_list)

for mail in result_list:
	print(mail)