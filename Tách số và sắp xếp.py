a = []
for t in range(int(input())):
    b = input()
    c = ""
    for i in range(len(b)):
        if b[i]<'0' or b[i]>'9':
            c+=' '
        else:
            c+=b[i]
    for i in c.split():
        a.append(int(i))
a.sort()
for i in a:
    print(i)
