t = int(input())
while t>0:
    a = list(map(str,input().split(".")))
    ok="YES"
    if not len(a)==4:
        ok="NO"
    for i in a:
        if i.isdigit():
            if int(i)<0 or int(i)>255:
                ok="NO"
                break
        else:
            ok="NO"
            break
    print(ok)
    t-=1