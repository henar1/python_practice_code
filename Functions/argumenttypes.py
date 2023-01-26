# Python Support different type of arguments
#1. Default Arguments: Its a parameter that assumes a default value is not provided in the function call of that argument
# Example
def myFuction(x, y=50):
    print("x :", x)
    print("y :", y)

# Driver code
# Here we call myFunction with only one argument
myFuction(10)

#2. Keyword Arguments
# Here the function caller needs to specify the argument name with values so that caller does not needs to 
# remember the order of parametres
# Example
def student(firstname, lastname):
    print(firstname, lastname)

# driver code
student(firstname='Wednesday', lastname='Adams')
student(lastname='Adams', firstname='Wednesday')

#3. Variable-length Arguments
# In Python we can pass variable number of arguments to a function using special symbols.
# There are two special symbols:
#    1. *args (Non-Keyword Arguments)
#    2. **kwargs (Keyword Arguments)
# Example with Variable length non-keyword argument
def myFun(*argv):
    for arguments in argv:
        print(arguments)

# Driver Code
myFun('Print this:', 'Be regular', 'Be carefree', 'Be cautious', 'Be grateful')

# Example with Variable length keyword arguments
def myFun1(**kwargs):
    for key , value in kwargs.items():
        print("%s == %s" % (key, value))

# driver code
myFun1(Date='Today', Day='Thursday', Time='Afternoon')




    
