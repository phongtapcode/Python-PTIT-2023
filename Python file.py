a = input()
ok="yes"
if a[-3:]!=".py" and len(a)<3:
    ok="no"
for i in range(0,len(a)-3):
    if not a[i].isalpha() and a[i]!='_':
        ok="no"
print(ok)

        

