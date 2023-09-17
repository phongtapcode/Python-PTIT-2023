import math
a,b = map(int,input().split())
for i in range(a,b-1,1):
    for j in range(i,b,1):
        for k in range(j,b+1,1):
            if math.gcd(i,j)==1 and math.gcd(j,k)==1 and math.gcd(k,i)==1:
                print("({}, {}, {})".format(i,j,k))