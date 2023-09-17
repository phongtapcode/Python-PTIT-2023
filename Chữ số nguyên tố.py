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
    dem=0
    for i in range(len(a)):
        if checksnt(int(a[i])):
            dem+=1
    
    if checksnt(len(a)) and dem>len(a)-dem:
        print("YES")
    else:
        print("NO")
    t-=1
