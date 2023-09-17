import math
n = int(input())
a = list(map(int,input().split()))
def checksnt(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
cnt = [0]*1000000
check = [False]*1000000
b = []
my_set=set()
for i in range(len(a)):
    if checksnt(a[i]):
        cnt[a[i]]+=1
        if not a[i] in my_set:
            my_set.add(a[i])
            b.append(a[i])
for i in range(len(b)):
    print(b[i],end=' ')
    print(cnt[b[i]])
    

        
    

