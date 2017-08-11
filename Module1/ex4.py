#Exercise 4: In this exercise you will create a program that reads a letter of the 
#alphabet from the user. If the user enters a, e, i, o or u then your program 
#should display a message indicating that the entered letter is a vowel. 
#If the user enters y then your program should display a message indicating 
#that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your 
#program should display a message indicating that the letter is a consonant.

def letteroutput():
    
    user_input_char = input("Please, enter the letter of your choice:   ")
    
    print(user_input_char)
    
    
    if user_input_char == "a" or "e" or "i" or "o" or "u":
            print ("The entered letter is a vowel")
    
    elif user_input_char == "y":
            print ("The entered letter is sometimes vowel and sometimes consonant")
        
    else:
            print ("The entered letter is consonant")

letteroutput()
