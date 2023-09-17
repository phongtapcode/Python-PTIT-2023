import math
t = int(input())
while t>0:
    a = int(input())
    b = list(map(int,input().split()))
    c = [0]*1000000
    
    for i in range(len(b)):
        c[b[i]]+=1
    for i in range(len(b)):
        if c[b[i]]%2==1:
            print(b[i])
            break
    t-=1