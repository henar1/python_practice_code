if __name__ == '__main__':
    stu=[]
    for _ in range(int(input("Enter value :"))):
        name = input("Enter value :")
        score = float(input("Enter value :"))
        stu.append([score,name])
    stu.sort()
    c=[]
    for j in stu:
        c.append(j[0])
    c=sorted(list(set(c)))
    semx = c[1]
    for i in stu:
        if semx == i[0]:
            print(i[1])