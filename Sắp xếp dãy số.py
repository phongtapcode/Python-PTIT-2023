for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    Max = max(a)
    for i in range(len(a)):
        if a[i]==Max:
            a.insert(i,k)
            break
    for i in a:
        if i<0:
            print(i,end=" ")
    for i in a:
        if i>=0:
            print(i,end = " ")
    print()