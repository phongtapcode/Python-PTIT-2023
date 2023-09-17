import math
n = int(input())
a = list(map(int,input().split()))
def checksnt(n):
    if n<2:
        return 0
    for i in range(2,int(math.sqrt(n)+1),1):
        if n%i==0:
            return 0
    return 1
snt = []
for i in range(n):
    if checksnt(a[i])==1:
        snt.append(a[i])
snt.sort()
dem=0
for i in range(n):
    if a[i] in snt:
        a[i]=snt[dem]
        dem+=1
    print(a[i],end=' ')
