t = int(input())
while t>0:
    x = input()
    k=x[0]
    dem=1
    for i in range(1,len(x),1):
        if x[i]==k:
            dem+=1
        else:
            print(dem,end='')
            print(k,end='')
            k=x[i]
            dem=1
    print(dem,end='')
    print(k,end='')
    t-=1