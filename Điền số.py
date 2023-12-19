t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    cnt = 0
    for i in range(1,len(arr)):
        if arr[i]-arr[i-1]>1:
            cnt+=arr[i]-arr[i-1]-1  
    print(cnt)