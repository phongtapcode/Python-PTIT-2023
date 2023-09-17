import math
t = int(input())

def reverse(a):
    dao=""
    for i in range(len(a)-1,-1,-1):
        dao+=a[i]
    return dao  

while t>0:
    x = input()
    y=reverse(x)
    if math.gcd(int(x),int(y))==1:
        print("YES")
    else:
        print("NO")
    t-=1


    