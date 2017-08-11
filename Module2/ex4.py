
# Exercise 4: One of the first known examples of encryption was used by Julius Caesar. 
# Caesar needed to provide written instructions to his generals, but he didn’t want his enemies 
# to learn his plans if the message slipped into their hands. As result, he developed what later became 
# known as the Caesar Cipher. The idea behind this cipher is simple (and as a result, 
# 	it provides no protection against modern code breaking techniques). Each letter in the 
# original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, 
# D becomes G, etc. The last three letters in the alphabet are wrapped around to the beginning: 
# X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher. 
# Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount, 
# and then display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. 
# Your program should also support negative shift values so that it can be used both to encode messages and decode messages. 
# Hints: ord(), chr()

def caesar_cipher(string):

	#user_input1 = input("input the letter you want to know the code for: ")

	final_string = ""
	for character in string:
		if ord(character) in range (65,91) or ord(character) in range(97,123):
			if character.upper() == character:
				new_value = ord(character)+3

				if new_value > 90:
					new_value = new_value - 90 + 65

				final_string += chr(new_value)

			elif character.lower() == character:

				new_value = ord(character) + 3
				if new_value > 122:
					new_value = new_value - 122 + 96
				final_string += chr(new_value)

			else:
				final_string += character

	print("Original: {}\n New: {}".format(string, final_string))

caesar_cipher("thisistring")