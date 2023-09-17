import math
n = int(input())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
k = int(input())
demtren=0
for i in range(0,n-1,1):
    for j in range(i+1,n,1):
        demtren+=a[i][j]
demduoi=0
for i in range(1,n,1):
    for j in range(0,i,1):
        demduoi+=a[i][j]
if abs(demduoi-demtren)<=k:
    print("YES")
    print(abs(demduoi-demtren))
else:
    print("NO")
    print(abs(demduoi-demtren))
    