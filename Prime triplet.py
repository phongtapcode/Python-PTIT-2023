prime = [1]*1000001
def sang():
    prime[1] = prime[0] = 0
    for i in range(2,1001):
        if prime[i]==1:
            for j in range(i*i,1000001,i):
                prime[j]=0
sang()
for t in range(int(input())):
    n = int(input())
    cnt=0
    for i in range(11,n):
        if prime[i] and prime[i-2] and prime[i-6] or (prime[i] and prime[i-4] and prime[i-6]):
            cnt+=1
    print(cnt)