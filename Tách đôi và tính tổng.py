a = input()

while len(a)>1:
    pos = int(len(a)/2)
    a = str(int(a[0:pos])+int(a[pos:]))
    print(a)