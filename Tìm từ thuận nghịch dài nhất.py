d = dict()
Max = -1  

file = open('VANBAN.in', 'r')
for line in file:
    a = line.split()
    for x in a:
        if x == x[::-1]:
            Max = max(Max, len(x))
            if x in d: d[x] += 1
            else: d[x] = 1

for x, y in d.items():
    if len(x) == Max: print(x + " " + str(d[x]))