a = input()
dem=0
ok=1
if len(a)==1:
    ok=0
if a[0]=='-':
    a = a[1:]
    while len(a)>1:
        tong=0
        for i in range(len(a)):
            tong+=int(a[i])
        a = str(tong)
        dem+=1
else:
    while len(a)>1:
        tong=0
        for i in range(len(a)):
            tong+=int(a[i])
        a = str(tong)
        dem+=1
if ok==0:
    print(1)
else:
    print(dem)
