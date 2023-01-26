# It is used to execute a block of statements repeatedly until a given condition is satisfied.
# when condition become false, the line immediately after the loop in the program is executed.
# Python uses indentation as its method of grouping statements. 
count = 0
while (count < 3):
    count = count + 1
    print("Success")

# Single statement while block
count = 0
while (count == 0): print("singleblock whileloop")

# It is suggested not to use this type of loops as it is a never ending infinite loop where the condition is 
# always true and you have to forcefully terminate the compiler.
