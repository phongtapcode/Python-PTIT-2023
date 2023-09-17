a = input()
dem=0
for i in range(len(a)):
    if a[i]=='4' or a[i]=='7':
        dem+=1
if dem==4 or dem==7:
    print("YES")
else: 
    print("NO")
