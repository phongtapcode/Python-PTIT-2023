t= int(input())
while t>0:
    a = input()
    if a[0]==a[len(a)-2] and a[1]==a[len(a)-1]:
        print("YES")
    else:
        print("NO")
    t-=1
