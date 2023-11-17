def check(a):
    if len(a)%2==1 or a!=a[::-1]:
        return False
    for i in a:
        if int(i)%2==1:
            return False
    return True
for t in range(int(input())):
    for i in range(22,int(input()),2):
        if check(str(i)):
            print(i,end=" ")
    print()