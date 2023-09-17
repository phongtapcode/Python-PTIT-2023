for t in range(int(input())):
    a = sorted(input())
    b=sorted(input())
    ok="NO"
    if a==b:
        ok="YES"
    print("Test "+str(t+1)+": "+ok)