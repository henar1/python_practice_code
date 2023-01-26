#stdin can be used to get input directly from command line, used for getting standard input, internally calls input() menthod
#automatically adds '\n' after each sentence
#we can take input in python in multiple ways:
#1. sys.stdin, input(), fileinput.input()
#1. sys.stdin: read input from stdin in Python using: import sys, sys.stdin helps to get input directly from command line
#2. input() can be used to take input from the user while executing the program and also in middle of execution
#3. fileinput.input(): we use this to read more than one file at a time, 2 method for using, first: importileinput,
# conti.. we pass the name of the files as a tuple in the “files” argument. Then we loop over each file to read it. 
# “sample.txt” and “no.txt” are two files present in the same directory as the Python file.
# second: Reading multiple files by passing file names from command line using fileinput module 
# Here, we pass the file name as a positional argument in the command line. fileargument parses the argument and reads the file and displays the content of the file.

# important: run 3rd type by commenting 1st type
# import sys
import fileinput
# 1st type
# for line in sys.stdin:
#     if 'q' == line.strip():
#         break
#     print(f'Input : {line}')
# print("Exit")

# 2nd type
inp = input("type anything")
print(inp)

#3rd type
with fileinput.input(files=('sample.txt', 'to.txt')) as f:
    for line in f:
        print(line)

