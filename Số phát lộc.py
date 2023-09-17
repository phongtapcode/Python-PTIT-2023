t = int(input())

while t>0:
    x=input()
    ok="YES"
    if x[len(x)-1]!='6' or x[len(x)-2]!='8':
        ok="NO"
    print(ok)
    t-=1