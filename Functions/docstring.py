# the first string after the function is called Document String or Docstring in short
# This is used to describe the functionality of a function.
# the use of Docstring is optional.
# syntax
# print(function_name.__doc__)
# Example: Adding Docstring to a function
def evenOdd(x):
    
    # if we skip this triple quote line, the output would be None
    """Function to check if the number is even or odd"""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# Driver code to call a function
print(evenOdd.__doc__)

