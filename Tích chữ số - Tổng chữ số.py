import math
t = int(input())

while(t>0):
    a = input()
    dem=0
    tongle=0
    tichchan=1
    for i in range(len(a)):
        if i%2==1:
            tongle+=int(a[i])
        else:
            if int(a[i])!=0:
                tichchan*=int(a[i])
                dem+=1
    if dem==0:
        tichle=0
    print(tichchan,end=' ')
    print(tongle)
    t-=1
