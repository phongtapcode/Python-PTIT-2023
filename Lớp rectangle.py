class Rectangle:
    def __init__(self,a,b,colo):
        self.a = a
        self.b = b
        self.colo = colo
    def perimeter(self):
        return (self.a+self.b)*2
    def area(self):
        return (self.a*self.b)
    def color(self):
        self.colo = self.colo.lower()
        x = ""
        x+=self.colo[0].upper()
        for i in range(1,len(self.colo),1):
            x+=self.colo[i]
        return x
arr = input().split()
if int(arr[0])>0 and int(arr[1])>0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")