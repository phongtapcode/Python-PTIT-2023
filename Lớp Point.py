import math
    class Point:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def distance(self,point2):
            return "{:.4f}".format(math.sqrt(math.pow(self.y-point2.y,2)+math.pow(self.x-point2.x,2)))
    def Decimal(a):
        return float(a)
if __name__ == '__main__':
t = int(input())
while t > 0:
    arr = input().split()
    p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
    p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
    print(p1.distance(p2))
    t -= 1