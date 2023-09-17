import math
t = int(input())
def check(n):
    if n%3==0:
        return "YES"
    return "NO"
while t>0:
    a = input()
    sum=0
    for i in range(len(a)):
        sum+=int(a[i])
    print(check(sum))
    t-=1