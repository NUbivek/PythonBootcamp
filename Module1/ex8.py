#Exercise 8: Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

def fizbuzz():

    for iter_num in range(1,101):
        if iter_num%3 == 0:
            print("Fizz")
        elif iter_num%5 == 0:
            print("Buzz")
        elif iter_num%3 == 0 and iter_num%5 == 0:
            print("FizzBuzz")
        else:
            print("NA")
fizbuzz()
