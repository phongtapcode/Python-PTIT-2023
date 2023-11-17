for t in range(int(input())):
    n = int(input())
    dic = {}
    cnt=0
    for i in range(n):
        a = input()
        if a in dic:
            dic[a]+=1
        else:
            dic[a]=1
        cnt = max(dic[a],cnt)
    key=1000
    for i in dic:
        if dic[i]==cnt:
            key=min(key,int(i))
    print(key)