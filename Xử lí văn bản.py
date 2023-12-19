from sys import stdin
dau = "?!"
arr = []
for line in stdin:
    line = line.strip()
    for i in dau:
        line = line.replace(i,".")
    a = line.split(".")
    for i in range(len(a)):
        cur = a[i].split()
        b = ""
        for j in cur:
            b += j.lower()+" "
        arr.append(b[0:1].upper()+b[1:])
for i in arr:
    if i!="":
        print(i)