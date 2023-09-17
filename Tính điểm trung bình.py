n = int(input())
a = list(map(float,input().split()))
min=10000000
max=0
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
    if a[i]>max:
        max=a[i]
dem=0
tong = 0
for i in range(len(a)):
    if a[i]!=min and a[i]!=max:
        tong+=a[i]
        dem+=1
print("{:.2f}".format(tong/dem))
        
    

