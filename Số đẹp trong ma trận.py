import math
n,m = map(int,input().split())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
max=0
min=100000
ok=0
for i in range(n):
    for j in range(m):
        if a[i][j]>max:
            max = a[i][j]
        if a[i][j]<min:
            min=a[i][j]
for i in range(n):
    for j in range(m):
        if a[i][j]==max-min:
            ok=1
            
if ok==0:
    print("NOT FOUND")
else:
    print(max-min)
    for i in range(n):
        for j in range(m):
            if a[i][j]==max-min:
                print(f"Vi tri [{i}][{j}]")


    