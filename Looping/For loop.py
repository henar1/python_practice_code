# these are used for sequential transversal
# Syntax
#for iterator_var in sequence:
    #statements(s)

n = 5 #integer
for i in range(0, n): #specified range
    print(i)

# Example with List, Tuple, string, and dictionary iteration using For Loops
# Iterating over a list
print("List of loops")
l = ["while", "for", "Nested"]
for i in l:
    print(i)

# Iterating over Tuple
print("\nTuple of loops")
l = ("while", "for", "Nested")
for i in l:
    print(i)

# Iterating over string
print("\nString of loops")
l = "loops"
for i in l:
    print(i)

#Iterating over dictionary
print("\nDictionary of loops")
d = dict()
d['xyz'] = 123
d['abc'] = 456
for i in d:
    print("%s , %d" % (i , d[i]))

# Iterating over a set
print("\nSet of loops")
set1 = {'while', 'for', 'Nested'}
for i in set1:
    print(i)

#Iterating by the index of sequence
# We can also use the index of elements in the sequence to iterate.
# calculate the length of the list
# Iterate over by keeping length of string in mind

list = ["while", "for", "nested"]
for index in range(len(list)):
    print (index)

# Using else statement with for loop

list = ["while", "for", "nested"]
for index in range(len(list)):
    print (index)
else:
    print("index not found")