# Exercise 2: A string is a palindrome if it is identical forward and backward. 
# For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. 
# Write a program that reads a string from the user and uses a loop to determines whether or not it is a palindrome. 
# Display the result, including a meaningful output message.

def palindrome_check():

	user_input1 = input("Input the number you want to check")
	user_input2 = ""

	for i in user_input1[::-1]:

		user_input2 += i

		