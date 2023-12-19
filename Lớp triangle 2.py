import math
t = int(input())
arr = []
for i in range(t):
    arr += [float(j) for j in input().split()]
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,td2):
        return math.sqrt((self.x - td2.x)*(self.x - td2.x) + (self.y - td2.y)*(self.y - td2.y))
i = 0
for _ in range(t):
    p1 = Point(arr[i],arr[i+1])
    p2 = Point(arr[i+2],arr[i+3])
    p3 = Point(arr[i+4],arr[i+5])
    a = p1.distance(p2)
    b = p2.distance(p3)
    c = p3.distance(p1)
    if a>=b+c or b>=a+c or c>=b+a:
        print("INVALID")
    else:
        print("{:.2f}".format(math.sqrt((a+b-c)*(a+b+c)*(b+c-a)*(c+a-b))/4))
    i+=6