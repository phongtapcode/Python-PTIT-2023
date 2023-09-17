a = input()
b = [False]*(len(a)+1)
n = len(a)
c = [0]*(len(a)+1)
def Try(s):
    if len(s)==n:
        print(s)
        return
    for i in range(n):
        if b[i]==False:
            b[i]=True
            Try(s+a[i])
            b[i]=False
Try("")