# Syntax of Python function with Parametres
# def function_name(parameter: data_type) -> return_type:
    #"""Doctring"""
    # body of the function
    #return expression

# Example
# Add two numbers and return

def add(num1: int, num2: int) -> int:
    # Add two  numbers
    sum = num1 + num2
    return sum

# Driver Code
num1, num2 = 5, 15
sum = add(num1, num2)
print(f"The addition of {num1} and {num2} results {sum}.")