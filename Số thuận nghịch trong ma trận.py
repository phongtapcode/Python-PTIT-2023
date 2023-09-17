import math
n,m = map(int,input().split())
def checkstn(a):
    if len(a)<2:
        return 0;
    for i in range(0,len(a)):
        if a[i]!=a[n-i-1]:
            return 0;
    return 1
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
max=0
ok=0
for i in range(n):
    for j in range(m):
        if checkstn(str(a[i][j]))==1 and a[i][j]>max:
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


    