import math
a,b = map(int,input().split())
dem=0
for i in range(pow(10,b-1),pow(10,b),1):
    if math.gcd(i,a)==1:
        print(i,end=" ")
        dem+=1
        if dem==10:
            print()
            dem=0