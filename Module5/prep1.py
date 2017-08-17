#user_input = str(input("Input the credit card number: "))

class Ccard():

	def __init__(self, user_input):

		self.user_input = user_input
		self.card_length = len(user_input)
		self.card_type = None
		#self.card_validation = None

	def check_card_length(self):

		if self.card_length == 15 or self.card_length == 16:
			return True
		else:
			raise Exception('Your credit card number is not valid. Check and enter again.')

	def type(self):

		Master_card_list = ["51","52","53","54","55"]
		Amex_card_list = ["34","37"]
		Discover_card_list = ["6011","65"]
		card_length = self.check_card_length() 
		

		

		if card_length == True:

			if self.user_input[0] == 4:
				self.card_type = "Visa"
				return self.card_type

			elif self.user_input[0:2] in Master_card_list:
				self.card_type = "Master Card"
				return self.card_type
				

			elif self.user_input[0:2] in Amex_card_list:
				self.card_type = "American Express"
				return self.card_type
				

			elif self.user_input[0:4] in Discover_card_list:
				self.card_type = "Discover"
				return self.card_type
				

			elif self.user_input[0:2] in Discover_card_list:
				self.card_type = "Discover"
				return self.card_type
				
			else:
				self.card_type = "Others"
				return self.card_type
				

# class Validation():

	def card_validation(self):

		#print(range(self.user_input[::-1]))

		rev_self_user_input = self.user_input[::-1]
		#print(rev_self.user_input)

		doubled_vals = []
		for doubled_val in rev_self_user_input[0::2]:
			# print(type(doubled_val))
			doubled_vals.append(2*int(doubled_val))
			 #return doubled_val

		# print (doubled_vals)
		# return True

		subnine_vals = []
		for i in doubled_vals:
			#print(i)
			if i >= 10:
				subnine_vals.append(i-9)
				#return subnine_val
			else:
				subnine_vals.append(i)
				#return subnine_val
		
		# print ("sub",subnine_vals)
		# return True

		sum_skipped_val = 0
		for sum_skipped_val in rev_self_user_input[1::2]:
			sum_skipped_val += sum_skipped_val
			#return sum_skipped_val

		if (int(sum_skipped_val) % 10) == 0:
			print ("The credit card transaction is valid and has been charged")
		else:
			print("The credit card transaction is not valid")

c1 = Ccard("8978678543678926")
print (c1.type())
print (c1.card_validation())



