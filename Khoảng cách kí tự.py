t = int(input())
def reverse(a):
    dao=""
    for i in range(len(a)-1,-1,-1):
        dao+=a[i]
    return dao
while t>0:
    x=input()
    ok="YES"
    y=reverse(x)
    for i in range(1,len(x)):
        if abs(ord(x[i])-ord(x[i-1])) != abs(ord(y[i])-ord(y[i-1])):
            ok="NO"
    print(ok)
    t-=1