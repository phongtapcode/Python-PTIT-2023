p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def ma(s):
    if s>='A' and s<='Z':
        return ord(s)-65
    if s=="_":
        return 26
    elif s==".":
        return 27
while True:
    a = list(map(str,input().split()))
    if a[0]=="0":
        break
    n = int(a[0])
    str1 = a[1]
    res = ""
    for i in str1:
        res+=p[(ma(i)+n)%28]
    print(res[::-1])