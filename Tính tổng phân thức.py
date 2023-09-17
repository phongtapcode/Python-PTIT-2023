t = int(input())

while t>0:
    a = int(input())
    b=0
    if a%2==1:
        for i in range(1,a+1,2):
            b+=float(1/i)
        print("{:.6f}".format(b))
    else:
        for i in range(2,a+1,2):
            b+=float(1/i)
        print("{:.6f}".format(b))
    t-=1