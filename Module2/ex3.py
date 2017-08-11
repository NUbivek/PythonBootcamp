#Exercise 3: Two words are anagrams if they contain all of the same letters, but in a different order. 
#For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and one v. 
#Create a program that reads two strings from the user, determines whether or 
#not they are anagrams, and reports the result.


def anagramss():

	user_input1 = str(input("enter the strings of your choice 1: "))
	user_input2 = str(input("enter the strings of your choice 2: "))

	input1_dict1 = {}
	for letter in user_input1:

		if letter not in input1_dict1:
			input1_dict1[letter] = 1

		else:
			input1_dict1[letter] += 1

	print("a",input1_dict1)

	input2_dict2 = {}
	for letter in user_input2:

		if letter not in input2_dict2:
			input2_dict2[letter] = 1

		else:
			input2_dict2[letter] += 1

	print("b",input2_dict2)



	if input1_dict1 == input2_dict2:
			print("anagrams")

	else:
			print("not anagrams")

anagramss()