# The else clause is only executed when your while condition becomes false
# if exception is raised, it won't be executed
# simillar to If- else


count = 0
while (count < 3):
    count = count + 1
    print("While loop printed")
else:
    print("else clause is printed")