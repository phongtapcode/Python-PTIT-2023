t = int(input())
d = dict() #Tạo dict rỗng
def check1(s): #Từ nào chứa ký tự đặc biệt, hoặc toàn số là số thì không cần xét đến nữa
	for i in s:
		if (not i.isdigit()) and (not i.isalpha()): return False
	if s.isdigit(): return False
	return True
def change(s): #Ví dụ như pt89it thì sẽ phải thành ptit. 
    check = 1
    for x in s:
        if x.isdigit(): s = s.replace(x, " ")
    a = s.split()
    res =""
    for x in a: res+=x
    return res
for i in range(t) : 
    s = input()
    s = s.lower()
    delim = ',.?!:;()-/'
    for x in delim: s = s.replace(x, ' ')
    a = list(s.split())
    for x in a:
        if(check1(x) and change(x)!=""):
            s1 = change(x)
            if s1 in d: d[s1]+=1 
            else: d[s1] = 1 
res = list(d.items())  # Lấy danh sách cặp (key, value) từ từ điển
res.sort(key = lambda x:(-x[1], x[0]))
for x in res: print(x[0], x[1], sep =" ")