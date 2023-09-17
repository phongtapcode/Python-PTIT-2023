a = input()
myset = set()
b=[]
for i in range(0,len(a)-1,2):
    if not a[i:i+2] in myset:
        myset.add(a[i:i+2])
        b.append(a[i:i+2])
for i in b:
    print(i,end=' ')