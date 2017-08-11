##Exercise 6: Write Python program to construct the following pattern, using a nested for loop.

def triangle():
    
    temp_var = ""
    for num in range(5):
            temp_var += "*"
            print(temp_var)
            
    for num in range(5,0,-1):
            temp_var = "*"
            print(num * "*")    
triangle()

##(optimized code below)

def triangle(number):
    for num in range (1, number+1):
        print (num*"*")
    for num in range (number-1,0,-1):
        print (num*"*")

triangle(6)

####

def triangle(number,character):
    character_str = str(character)
    for num in range (1, number+1):
        print (num*character_str)
    for num in range (number-1,0,-1):
        print (num*character_str)

triangle(6,"$")
