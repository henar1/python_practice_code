# In Python every variable name is reference
# When we pass the variable to a function, a new reference to a object is created
# Parameter passing in python same as reference passing in java
# Example

def myFuc(x): #here x is a new reference to same list lst
    x[0] = 34

#Driver code (Note that the lst is modified)
lst = [10, 11, 12, 13, 14, 15]
myFuc(lst) # If we comment this part, we will get output as a latter passed variables
print(lst)

# when we pass a refernece and change the recieved reference to something else, 
# the coonection between recieved and passed parameter is broken
# Example2
def myFun(x):
    x = [20, 30, 40, 50] # we haven't connected with latter part
# After this line link of x with previous oject gets broken. a new object is assigned to x

list = [10, 11, 12, 13, 14, 15]
myFun(list)
print(list)

# Example to demonstrate that the reference link is broken, if we assign a new a value
def myFun1(x):
    x = 20

x = [10, 11]
myFun1(x)
print(x)
