t = int(input())
def tong(a):
    tong1=1
    for i in range(len(a)):
        tong1*=int(a[i])
    return tong1

while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a = sorted(a,key=lambda x: (tong(str(x)),x))
    for i in range(n):
        print(a[i],end=' ')
    t-=1