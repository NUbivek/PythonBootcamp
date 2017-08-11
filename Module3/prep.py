#pseudo codes:

#1. Create a dictionary




def to_roman():
    n = int(input('Enter number: '))
    list_roman = [
        ('M', 1000), 
        ('CM', 900),
        ('D', 500),
        ('CD', 400), 
        ('C', 100),
        ('XC', 90), 
        ('L', 50),
        ('XL', 40), 
        ('X', 10),
        ('IX', 9), 
        ('V', 5),
        ('IV',4), 
        ('I', 1)
    ]
    result = ''
    for r_numeral, integer in list_roman:

	quot, remainder = divmod(inpt, integer)  
        if quot > 0:
            result += quot*r_numeral
            inpt = remainder      

###The while loop way of doing the same problem:
        # print(n, integer)
        # while n >= integer:
        #     result += numeral
        #     n -= integer
        #     print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))

    return result



print(to_roman())




	}
