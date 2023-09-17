t = int(input())
dem=0
while t>0:
    n = int(input())
    i = 2
    while n>1:
        if n%i==0:
            n/=i
            dem+=i
        else:
            i+=1
    t-=1
print(dem)
