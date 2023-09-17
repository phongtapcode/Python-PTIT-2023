import math
t = int(input())
def check(n):
    if n<2:
        return "NO"
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i==0:
            return "NO"
    return "YES"
while t>0:
    a = input()
    sum=0
    for i in range(len(a)):
        sum+=int(a[i])
    print(check(sum))
    t-=1