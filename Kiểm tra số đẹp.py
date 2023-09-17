t = int(input())

while t>0:
    a = input()
    x = a[0]
    y = a[1]
    ok = "YES"
    for i in range(2,len(a)-1,2):
        if a[i]!=x or a[i+1]!=y:
            ok="NO"
    if len(a)%2==1 and a[len(a)-1] != a[len(a)-3]:
        ok="NO"
        
    print(ok)
    t-=1