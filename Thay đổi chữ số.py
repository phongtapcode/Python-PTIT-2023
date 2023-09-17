t = int(input())

while t>0:
    x,y = map(str,input().split())
    a = input()
    b = input()
    if int(x)>int(y):
        y,x=x,y
    mina = ""
    minb = ""
    for i in range(len(a)):
        if a[i]==y[0]:
            mina+=x[0]
        else: 
            mina+=a[i]
    for i in range(len(b)):
        if b[i]==y[0]:
            minb+=x[0]
        else: 
            minb+=b[i]
    print(int(mina)+int(minb))
    maxa = ""
    maxb = ""
    for i in range(len(a)):
        if a[i]==x[0]:
            maxa+=y[0]
        else: 
            maxa+=a[i]
    for i in range(len(b)):
        if b[i]==x[0]:
            maxb+=y[0]
        else: 
            maxb+=b[i]
    print(int(maxa)+int(maxb))
    t-=1