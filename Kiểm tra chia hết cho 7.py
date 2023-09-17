t = int(input())
def reverse(a):
    a=str(a)
    dao=""
    for i in range(len(a)-1,-1,-1):
        dao+=a[i]
    return int(dao)
while t>0:
    a = input()
    tong=int(a)
    ok=0
    if tong%7==0:
        print(tong)
    else:
        for i in range(1000):
            if (tong+reverse(tong))%7==0:
                print(tong+reverse(tong))
                ok=1
                break
            else:
                tong+=reverse(tong)
        if ok==0:
            print("-1")
    t-=1
