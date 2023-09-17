a = input()
myset = set()
b=[]
cnt=[0]*100
for i in range(0,len(a)-1,2):
    cnt[int(a[i:i+2])]+=1
    if not a[i:i+2] in myset:
        myset.add(a[i:i+2])
        b.append(a[i:i+2])
b.sort()
for i in b:
        print(i,end=' ')
