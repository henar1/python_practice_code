#The provided code stub reads and integer, , from STDIN. For all non-negative integers i<n , print i(square).
#Here list of non-negative integers less than n<3 are [0,1,2], we need to print square of each number on seperate line

#looping would be there
n = int(input("Enter the number :" ))
# i = 0
# while i < n:
#     print (i * i)
#     i += 1

#using range function
for i in range(n):
    print(i**2)
