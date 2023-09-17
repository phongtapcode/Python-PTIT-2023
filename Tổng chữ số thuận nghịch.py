t = int(input())
def check(n):
    if len(n)==1:
        return "NO"
    for i in range(len(n)):
        if n[i]!=n[len(n)-i-1]:
            return "NO";
    return "YES";
while t>0:
    a = input()
    sum=0
    for i in range(len(a)):
        sum+=int(a[i])
    print(check(str(sum)))
    t-=1