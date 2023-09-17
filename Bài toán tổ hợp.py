n,k = map(int,input().split())
a = list(map(int,input().split()))
myset = set()
for i in a:
    myset.add(i)
b = list(myset)
b.sort()
n=len(b)
a = [0]*(k+1)
def Try(i):
    for j in range(a[i-1]+1,n-k+i+1):
        a[i]=j
        if i==k:
            for h in range(1,k+1):
                print(b[a[h]-1],end=" ")
            print()
        else:
            Try(i+1)
Try(1)
        