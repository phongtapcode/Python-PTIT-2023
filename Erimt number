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
    for i in range(13,n):
        a = int(str(i)[::-1])
        if prime[i]==1 and prime[a]==1 and a>i and a<n:
            print(i,a,end=" ")
    print()