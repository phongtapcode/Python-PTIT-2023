n = int(input())
a = list(map(int,input().split()))
ok = 0
a.sort()
for i in range(1,len(a)):
    if a[i]-a[i-1]>1:
        print(a[i-1]+1)
        ok=1
        break
if ok==0:
    print(a[-1]+1)

