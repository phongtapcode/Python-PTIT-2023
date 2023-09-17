import math
n,m = map(int,input().split())
def checksnt(a):
    if a<2:
        return 0;
    for i in range(2, int(math.sqrt(a))+1,1):
        if a%i==0:
            return 0
    return 1
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
max=0
ok=0
for i in range(n):
    for j in range(m):
        if checksnt(a[i][j]) and a[i][j]>max:
            max = a[i][j]
            ok=1
if ok==0:
    print("NOT FOUND")
else:
    print(max)
    for i in range(n):
        for j in range(m):
            if a[i][j]==max:
                print(f"Vi tri [{i}][{j}]")


    