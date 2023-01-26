# Anonymous function in python mean a function withour name
# def keyword is used to define a normal function
# lambda keyword is used to create a anonymous function
# Example:
# Python code to illustrate the cube of the number using lambda function
def cube(x):
    return x*x*x  #Normal function
cube_v2 = lambda x : x*x*x # Creating a lambda function

print(cube(7))
print(cube_v2(7))
