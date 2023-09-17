n = int(input())
a=[]
for i in range(n):
    b = list(map(int,input().split()))
    a+=b
    if len(a)>=n:
        break
    
chan = []
le = []
b=[0]*(n+1)
for i in range(n):
    if(a[i]%2==0):
        chan.append(a[i])
    else:
        le.append(a[i])
chan.sort()
le.sort(reverse=True)
demchan=0
demle=0
for i in range(n):
    if a[i]%2==0:
        b[i]=chan[demchan]
        demchan+=1
    else:
        b[i]=le[demle]
        demle+=1
for i in range(n):
    print(b[i],end=" ")