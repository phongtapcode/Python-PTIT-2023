import math
n,m = map(int,input().split())
matran = []
for i in range(n):
    a = list(map(int,input().split()))
    matran.append(a)
def checksnt(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(n):
    for j in range(len(matran[i])):
        if checksnt(matran[i][j]):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
    

        
    

