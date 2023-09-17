t = int(input())

while t>0:
    a = input()
    c=""
    for i in range(len(a)):
        if a[i].isalpha():
            c+=a[i]
    d = sorted(c)
    c=""
    for i in range(len(d)):
        c+=d[i]
    a+="asdjf"
    b=""
    tong=0
    for i in range(len(a)-1):
        if a[i].isdigit():
            tong+=int(a[i])
    c+=str(tong)
    print(c)
    t-=1