n,m = map(int,input().split())
a=[]
def tn(a):
    if len(a)<2:
        return False
    for i in range(len(a)):
        if a[i]!=a[len(a)-i-1]:
            return False
    return True
for i in range(n):
    b = list(map(str,input().split()))
    a.append(b)
max=0
ok=0
for i in range(n):
    for j in range(m):
        if tn(a[i][j]) and int(a[i][j])>max:
            max = int(a[i][j])
            ok=1
if ok==0:
    print("NOT FOUND")            
else:
    print(max)
for i in range(n):
    for j in range(m):
        if int(a[i][j])==max:
            print("Vi tri [{}][{}]".format(i,j))