t = int(input())
while t>0:
    x=input()
    ok="YES"
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            ok="NO"
            break
    print(ok)
    t-=1