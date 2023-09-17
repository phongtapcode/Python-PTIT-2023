a= input()
inhoa=0
inthuong=0
for i in range(len(a)):
    if a[i]>='a' and a[i]<='z':
        inthuong+=1
    else:
        inhoa+=1
if inhoa<=inthuong:
    print(a.lower())
else:
    print(a.upper())
