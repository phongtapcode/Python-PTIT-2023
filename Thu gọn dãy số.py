n = int(input())
a = input().split()
i=0
while i<len(a)-1:
    if (int(a[i])+int(a[i+1]))%2==0:
        a.pop(i)
        a.pop(i)
        i=0
    else: 
        i+=1
print(len(a))