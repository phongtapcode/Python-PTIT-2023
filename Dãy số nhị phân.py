n = int(input())
a = list(map(int,input().split()))
ok = 0
for i in range(1,len(a),1):
    if a[i]!=a[i-1]:
        ok+=1
print(ok)