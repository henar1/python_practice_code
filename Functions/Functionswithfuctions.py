# A function i.e defined inside another function is known as inner functionor nested function.
# Nested functions are able to access variables of the enclosing scope.
# Inner functions are used so that they can be protected from everything happening outside the function.
# Example: Python program to demonstarte accessing of variables of nested functions

def f1():
    s = 'Lets learn new things'

    def f2():
        # s1 = 'new things' # if we want to execute function 2
        print(s)
        # print(s1) # if we want to execute function 2

    f2()

# driver's code
f1() 
