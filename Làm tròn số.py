for t in range(int(input())):
    arr = list(int(i) for i in input())
    for i in range(len(arr)-1,0,-1):
        if arr[i]>=5:
            arr[i-1]=arr[i-1]+1
        arr[i]=0
    for i in range(0,len(arr)):
        print(arr[i],end="")
    print()