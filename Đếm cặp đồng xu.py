def gt(n):
    tich =1
    for i in range(1,n+1):
        tich*=i
    return tich
n = int(input())
a = []
hang = [0]*n
cot = [0]*n
for i in range(n):
    a.append(list(input()))
for i in range(n):
    for j in range(n):
        if a[i][j]=='C':
            hang[i]+=1
            cot[j]+=1
cnt=0
for i in range(n):
    if hang[i]>=2:
        cnt+=gt(hang[i])/(2*gt(hang[i]-2))
for i in range(n):
    if cot[i]>=2:
        cnt+=gt(cot[i])/(2*gt(cot[i]-2))
print(int(cnt))
