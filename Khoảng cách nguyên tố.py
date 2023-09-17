primes = [True]*(1000000)
def sangsnt():
    primes[0]=primes[1]=False
    for num in range(2,1000,1):
        if primes[num]:
            for i in range(num*num,1000000,num):
                primes[i]=False
sangsnt()
cnt=0
n,x = map(int,input().split())
print(x,end=' ')
for i in range(2,10000):
    if cnt==n:
        break
    if primes[i]:
        print(x+i,end=' ')
        x+=i
        cnt+=1

