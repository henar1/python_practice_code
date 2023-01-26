#You are given  scores. Store them in a list and find the score of the runner-up.
#The first line contains n
if __name__ == '__main__':
    n = int(input("Enter value : "))
    #string into a list.
    arr =list(map(int, input("Enter value : ").split("Enter value : ")))
    arr.sort(reverse=True)
    #Syntax : fromkeys(seq, val)
    arr = list(dict.fromkeys(arr)) # using dict.fromkey() dictionary function with kwy mapped and specific value
    print(arr[1])
