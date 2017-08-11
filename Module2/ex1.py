# Exercise 1: A prime number is an integer greater than 1 that is only divisible by one and itself. 
# Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. 
# Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime. 
# Ensure that the main program will not run if the file containing your solution is imported into another program.

def primenumberss(input1):

	#input1 = int(input("Enter the number to test: "))

	if input1 == 1:
		return True

	elif input1 < 0:
		return False

	for check in range (2,input1):

		if input1 % check == 0:
			return False

print(primenumberss (3))


