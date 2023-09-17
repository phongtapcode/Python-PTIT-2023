t = int(input())
while t>0:
    a = input()
    a+="asdjf"
    b=""
    c = list()
    for i in range(len(a)-1):
        if a[i].isdigit() and a[i+1].isdigit():
            b+=a[i]
        elif a[i].isdigit() and not a[i+1].isdigit():
            b+=a[i]
            c.append(b)
            b=""
    max = 0
    for i in c:
        if int(i)>max:
            max=int(i)
    print(max)
    t-=1    