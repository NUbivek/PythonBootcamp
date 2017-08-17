# The algorithm divides the input list into two parts: 
# the sublist of items already sorted, which is built up from left to right at 
# the front (left) of the list, and the sublist of items remaining to be sorted 
# that occupy the rest of the list. Initially, the sorted sublist is empty and 
# the unsorted sublist is the entire input list. The algorithm proceeds by finding 
# the smallest (or largest, depending on sorting order) element in 
# the unsorted sublist, exchanging (swapping) it with the leftmost unsorted 
# element (putting it in sorted order), and moving the sublist boundaries one 
# element to the right.

def selection_sort(user_input):

	user_input_sorted = []
	user_input_remaining = []

# finding minimum

	smallest_remaining = min(user_input_remaining)

##swap
	smallest_remaining, smallest_sorted = smallest_sorted,smallest_remaining


	
	mid = round(len(user_input)//2)




