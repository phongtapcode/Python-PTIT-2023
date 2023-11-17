import math
t = int(input())
class Toado:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,toado2):
        return float(math.sqrt(math.pow(self.y-toado2.y,2)+math.pow(self.x-toado2.x,2)))
a = []
while t>0:
    x1,y1,x2,y2,x3,y3 = map(float,input().split())
    td1 = Toado(x1,y1)
    td2 = Toado(x2,y2)
    td3 = Toado(x3,y3)
    canh1 = td1.distance(td2)
    canh2 = td2.distance(td3)
    canh3 = td3.distance(td1)
    if canh1+canh2<=canh3 or canh1+canh3<=canh2 or canh2+canh3<=canh1:
        a.append("INVALID")
    else:
        a.append("{:.3f}".format(canh1+canh2+canh3))
    t-=1

for i in range(0,len(a)):
    print(a[i])