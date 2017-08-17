# Write your Bubble Search function.

# A bubble sort is a sorting algorithm with a Big O complexity of O(n**2). 
#It is called bubble sort, because the small numbers "bubble" to the top of the list.
# The general flow is to step through the list, continually comparing pairs of numbers.
# If the number on the left is larger than the number on the right, swap them and continue.

# Write a function, bubble_sort(), that takes an list. 
#It should return a sorted list, using the bubble sort algorithm.

# alist = [54,26,93,17,77,31,44,55,20]

def bubble_search(user_input_list):

	if len(user_input_list) > 1:	

	#left_letters = []
		for j in range(len(user_input_list)-1):
			for i in range(len(user_input_list)-1):
				if user_input_list[i] > user_input_list[i+1]:
					user_input_list[i],user_input_list[i+1] = user_input_list[i+1],user_input_list[i]
				else:
					pass

	return user_input_list

		# for j in str(user_input_list[i]):
		# 	#split_number = user_input_list[]


x= bubble_search([54,26,93,17,77,31,44,55,20])
#print ([54,26,93,17,77,31,44,55,20])
print(x)
