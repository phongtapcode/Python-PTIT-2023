for t in range(int(input())):
    hang,cot = map(int,input().split())
    a = []
    for i in range(hang):
        a.append(list(map(int,input().split())))
    b = [[0]*hang for _ in range(cot)]
    for i in range(cot):
        for j in range(hang):
            b[i][j]=a[j][i]
    tich = [[0]*hang for _ in range(hang)]
    for i in range(hang):
        for j in range(hang):
            for k in range(cot):
                tich[i][j]+=a[i][k]*b[k][j]
    for i in range(hang):
        for j in range(hang):
            print(tich[i][j],end=" ")
        print()
