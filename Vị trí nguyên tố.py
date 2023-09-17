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
    for i in range(len(a)):
        if checksnt(i) and not checksnt(int(a[i])):
            ok=0
        if not checksnt(i) and checksnt(int(a[i])):
            ok=0
    if ok==1:
        print("YES")
    else:
        print("NO")
    t-=1