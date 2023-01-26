# import os
# import random
# import re
# import sys


# if __name__ == '__main__':
n = int(input("Enter a number: "))
    
#If  is odd, print Weird
if n % 2 != 0:
    print('Weird')
else:
    if n >= 2 and n <= 5: #If  is even and in the inclusive range of 2 to 5 , print Not Weird
        print('Not Weird')
    elif n >= 6 and n <= 20: # If  is even and in the inclusive range of 6 to 20, print Weird
        print('Weird')
    else:
        print('Not Weird') # If  is even and greater than , print Not Weird