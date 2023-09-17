a = input()
my_set = set()
dem=0
while len(a)>0:
    b = list(map(int,a.split()))
    dem+=len(b)
    for i in range(len(b)):
        b[i]%=42
        my_set.add(b[i])
    if dem>=10:
        break
    a = input()
print(len(my_set))
