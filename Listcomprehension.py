# Print the list in lexicographic increasing order.
# its kind of dictioanary order

if __name__ == '__main__':
    x = int(input("Enter_value: "))
    y = int(input("Enter_value: "))
    z = int(input("Enter_value: "))
    n = int(input("Enter_value: "))
    
    list_comp = list([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n ])
    print(list_comp)