from math import log2
import math
t = int(input())
BASE = "0123456789ABCDEF"
while t>0:
    num,base = map(str,input().split())
    base = int(log2(int(base)))
    num = bin(int(num))[2:]
    while len(num)%base:
        num="0"+num
    hs=""
    for i in range(0,len(num),base):
        b = num[i:i+base]
        dem=0
        cong=0
        for j in range(len(b)-1,-1,-1):
            cong+=int(b[j])*int(math.pow(2,dem))
            dem+=1
        hs+=BASE[cong]
    print(hs)
    t-=1
