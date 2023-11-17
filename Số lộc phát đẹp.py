def check(a):
    if a[0]=='8':
        return False
    for i in range(len(a)):
        if a[i]!='6' and a[i]!='8':
            return False
        if a[i]=='8' and a[i:i+3]=='888':
            return False
    return True
if check(input()):
    print("YES")
else:
    print("NO")