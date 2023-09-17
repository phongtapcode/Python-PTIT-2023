t = int(input())
while t>0:
    x = input()
    for i in range(len(x)):
        if x[i].isdigit():
            for h in range(int(x[i])):
                print(x[i-1],end='')
    t-=1