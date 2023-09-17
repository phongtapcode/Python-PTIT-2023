t = int(input())

while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0]*1000000
    for i in range(0,len(a)):
        cnt[a[i]]+=1
    min = 1000000
    ok=1
    for i in range(0,len(a)):
        if cnt[a[i]]>n/2 and a[i]<min:
            min=a[i]
            ok=0
    if ok==0:
        print(min)
    else:
        print("NO")
    
    t-=1

