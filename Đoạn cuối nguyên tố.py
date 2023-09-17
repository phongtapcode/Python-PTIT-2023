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
    n = input()
    dem=n[-4:]
    if checksnt(int(dem)):
        print("YES")
    else:
        print("NO")
    t-=1