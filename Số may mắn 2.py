t = int(input())
while(t>0):
    a = input()
    ok="YES"
    for i in range(len(a)):
        if a[i]!='4' and a[i]!='7':
            ok="NO"
    print(ok)
    t-=1


