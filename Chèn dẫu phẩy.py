x = input()
j=0
new=""
for i in range(len(x)-1,-1,-1):
    new+=x[i]
    j+=1
    if j==3 and i!=0:
        new+=','
        j=0
for i in range(len(new)-1,-1,-1):
    print(new[i],end='')

    