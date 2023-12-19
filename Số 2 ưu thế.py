from collections import deque

s = "012"
v = []

def check(s):
    count = {}
    if s.count("2") > len(s) // 2: return True
    else: return False

def gen():
    q = deque()
    q.append("1")
    q.append("2")
    v.append("2")
    while True:
        x = q.popleft()
        if len(v) == 1005: break
        for i in s:
            s1 = x + i
            q.append(s1)
            if check(s1): v.append(s1)


t = int(input()) 
gen()
for _ in range(t):
    n = int(input()) 
    for i in range(n): print(v[i], end=" ")
    print()