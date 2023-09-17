import math
t = int(input())
def checksnt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i==0:
            return False
    return True
while(t>0):
    a = input()
    ok=1
    tong=0
    for i in range(len(a)):
        tong+=int(a[i])
        if i%2==0 and int(a[i])%2!=0:
            ok=0
        if i%2==1 and int(a[i])%2!=1:
            ok=0
    if ok==1 and checksnt(tong):
        print("YES")
    else:
        print("NO")
    t-=1