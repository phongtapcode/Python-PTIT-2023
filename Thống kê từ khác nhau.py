t = int(input())
dic = dict()
def check(s):
	for i in s:
		if (not i.isdigit()) and (not i.isalpha()): return False
	return True
for _ in range(t):
    s = input()
    s = s.lower()
    delim = ',.?!:;()-/'
    for x in delim:
        s = s.replace(x," ")
    a = list(s.split())
    for i in a:
        if check(i):
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
b = list(dic.items())    
b.sort(key= lambda x: (-x[1],x[0]))
for i in b:
    print(i[0],i[1])
