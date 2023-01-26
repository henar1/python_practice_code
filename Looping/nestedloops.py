# when one loop is stated within another loops, loop type would not matter
# syntax for for loop
# for iterator_var in sequence:
#    for iterator_var in sequence:
#        statements(s)
#        statements(s)
# syntax for while loop
#while expression:
  # while expression: 
#       statement(s)
#       statement(s)
#for nested loop
# from __future__ import print_function
for i in range(1 , 5):
    for j in range(i):
        print(i, end='') #end character has been identified by whitespace not new line
    print()

