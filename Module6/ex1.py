# Exercise 1.
# Write your Binary Search function.

# Start at the middle of your dataset. If the number you are searching for is lower, 
#stop searching the greater half of the dataset. Find the middle of the lower half 
#and repeat.

# Similarly if it is greater, stop searching the smaller half and repeat
# the process on that half. By continuing to cut the dataset in half, 
#eventually you get your index number.

# Number to search for - 3 alist = [1,2,3,4,5,6,7]

def binary_search (user_input,x):

	# user_input_lefthalf = 0
	# user_input_righthalf = 0
	
	mid = round(len(user_input)//2)
	#print (mid)
	#print (user_input[mid-1])

	while len(user_input) > 1:

		if x == user_input[mid-1]:

			value = x
			print("The value is {}", x)
			return x

		elif x < user_input[mid-1]:

			start_point = user_input[0]
			end_point = user_input[mid-1]
			value = len(range(user_input[start_point:end_point]))//2
			print (value)
			return value

		elif x > user_input[mid-1]:

			start_point = user_input[mid-1]
			end_point = user_input[:]
			value = len(range(user_input[start_point:end_point]))//2
			print (value)
			return value
	

binary_search([1,2,3,4,5,6,7],6)






