a = input()
b = input()
a = a.lower()
b = b.lower()
a1 = set(a.split())
a2 = set(b.split())
giao = list(a1&a2)
hop = list(a1|a2)
giao.sort()
hop.sort()
for i in hop:
    print(i,end=" ")
print()
for i in giao:
    print(i,end=" ")
