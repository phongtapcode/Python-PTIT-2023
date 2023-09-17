x,y,z = map(int,input().split())
ok=0
for i in range(1,z-x,1):
    if (x+i)%y==0:
        ok=1
        for j in range(x+i,z,y):
            print(j-x,end=' ')
        break
if ok==0:
    print("-1")