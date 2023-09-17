t=int(input())

while t>0:
    x=int(input())
    i=2
    dem=0
    print("1 * ",end='')
    while x>1:
        if x%i==0:
            dem+=1
            x/=i
        else:
            if dem!=0:
                print(f"{i}^{dem} * ",end='')
            i+=1
            dem=0
    print(f"{i}^{dem}")
    t-=1


    