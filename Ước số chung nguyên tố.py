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
    a,b = map(int,input().split())
    c=str(math.gcd(a,b))
    dem=0
    for i in range(len(str(c))):
        dem+=int(c[i])
    if checksnt(dem):
        print("YES")
    else:
        print("NO")
    t-=1
