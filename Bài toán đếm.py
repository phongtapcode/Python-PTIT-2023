n = int(input())
a = []
while True:
    if len(a)>=n:break
    b = list(map(int,input().split()))
    for i in range(len(b)):
        a.append(b[i])
a.sort()
ok=1
for i in range(1,a[n-1]):
    if not i in a:
        print(i)
        ok=0
if ok==1:print("Excellent!")