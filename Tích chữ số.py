import math
t = int(input())
def check(n):
    tich=1
    for i in range(len(n)):
        if n[i]!='0':
            tich*=int(n[i])
    return tich
while t>0:
    a = input()
    print(check(a))
    t-=1