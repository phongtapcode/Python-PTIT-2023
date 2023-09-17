import math
n = int(input())
matran = []
for i in range(n):
    a = list(map(int,input().split()))
    matran.append(a)
k = int(input())
tongtren = 0
tongduoi = 0
for i in range(0,n):
    for j in range(i+1,n):
        tongtren+=matran[i][j]
for i in range(1,n):
    for j in range(0,i):
        tongduoi+=matran[i][j]
if abs(tongduoi-tongtren)<=k:
    print("YES")
    print(abs(tongduoi-tongtren))
else:
    print("NO")
    print(abs(tongduoi-tongtren))
    

        
    

