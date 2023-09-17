import math
t = int(input())
def check(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i==0:
            return 0
    return 1
while t>0:
    a = input()
    a2 = a[0:3]
    a1 = a[-3:]
    if check(int(a1))==1 and check(int(a2))==1:
        print("YES")
    else:
        print("NO")
    t-=1