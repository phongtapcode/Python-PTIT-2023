from sys import stdin
for line in stdin:
    if len(line)>0:
        cur = line.strip().lower().split()
        a = ""
        for i in cur:
            a+=i+" "
        if a[len(a)-2]!="." and a[len(a)-2]!="!" and a[len(a)-2]!="?":
            a = a+"."
        a = a.replace(" ?","?")
        a = a.replace(" !","!")
        a = a.replace(" .",".")
        a = a[0:1].upper() + a[1:]
        print(a)