t = int(input())

while t>0:
    a = input()
    b = "0"
    ok="YES"
    for i in range(1,len(a)):
        if int(a[i])>int(a[i-1]):
            b+="0"
        elif int(a[i])<int(a[i-1]):
            b+="1"
        else:
            ok="NO"
    if ok=="NO":
        print(ok)
    else:
        dem=0
        for i in range(1,len(b)):
            if int(b[i])==1 and int(b[i-1])==0:
                dem+=1
        if dem==1:
            print("YES")
        else:
            print("NO")
    t-=1
