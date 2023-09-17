t = int(input())
while t>0:
    a = input()
    ok = "YES"
    for i in range(len(a)):
        if a[i]!='0' and a[i]!='1' and a[i]!='2':
            ok="NO"
    print(ok)
    t-=1