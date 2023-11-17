t,k = map(int,input().split())
dic = dict()
def change(s):
    for i in s:
        if i.isdigit():
            s = s.replace(i," ")
    a = list(s.split())
    x=""
    for i in a:
        x+=i
    return x
for _ in range(t):
    s = input()
    s = s.lower()
    delim = ',.?!:;()-/'
    for x in delim:
        s = s.replace(x," ")
    a = list(s.split())
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
b = list(dic.items())    
b.sort(key= lambda x: (-x[1],x[0]))
for i in b:
    if i[1]>=k:
        print(i[0],i[1])
