t = int(input())

while t>0:
    x=input()
    ok = "YES"
    tong = 0
    for i in range(len(x)-1):
        tong+=int(x[i])
        if abs(int(x[i])-int(x[i+1]))!=2:
            ok="NO"
            break
    if (tong+int(x[len(x)-1]))%10!=0:
        ok="NO"
    print(ok)
    t-=1