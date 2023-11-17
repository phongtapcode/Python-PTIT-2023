n = int(input())
a = list(map(int,input().split()))

a.sort()
m = max(a[n-1]*a[n-2],a[0]*a[1])
m = max(a[n-1]*a[n-2]*a[n-3],m)
m = max(m, a[0]*a[1]*a[2])
m = max(a[0]*a[1]*a[n-1],m)
print(m)