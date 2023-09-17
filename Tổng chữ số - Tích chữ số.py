import math
t = int(input())

while(t>0):
    a = input()
    dem=0
    tongchan=0
    tichle=1
    for i in range(len(a)):
        if i%2==0:
            tongchan+=int(a[i])
        else:
            if int(a[i])!=0:
                tichle*=int(a[i])
                dem+=1
    if dem==0:
        tichle=0
    print(tongchan,end=' ')
    print(tichle)
    t-=1
