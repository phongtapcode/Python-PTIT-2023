t = int(input())

while t>0:
    a=input()
    ok = "YES"
    b = a[0]
    if len(a)%2==0 or a[0]==a[1]:
        ok="NO"
    for i in range(2,len(a),2):
        if a[i]!=b:
            ok="NO"
            break
    print(ok)
    t-=1