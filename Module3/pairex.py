 # If a word begins with a vowel, append “yay” to the end of the word.
 #  If a word begins with a consonant, remove all the consonants 
 #  from the beginning up to the first vowel and append them to the end of the word. 
 #  Finally, append “ay” to the end of the word.




#Rules:
#1: vowel, we append yay at the end
	## vowel_list = ["a","e","i","o","u"]
	## if user_input[1] in vowel_list:

def piglatinn():

	user_input = str(input("Enter the word you want to convert: "))

	vowel_list = ["a","e","i","o","u"]
	
	if user_input[0] in vowel_list:
			new_word = user_input + "yay"
	#print (new_word)

	else:
		for letter in user_input:
			if letter in vowel_list:
				stopping_point = user_input.find(letter)
				break
			#(user_input[0], when user_input == vowel_list temp_var)
		
		new_word = user_input[stopping_point:] + user_input[0:stopping_point] + "yay"
		print (new_word)
		
piglatinn()