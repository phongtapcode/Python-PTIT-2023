t = int(input())
while t>0:
    n,a = map(int,input().split())
    b = input().split()
    for i in range(a,n,1):
        print(b[i],end = ' ')
    for i in range(0,a,1):
        print(b[i],end=' ')
    t-=1