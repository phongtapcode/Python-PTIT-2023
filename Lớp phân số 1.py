import math

class Phanso:
    def __init__(self,ts,ms):
        self.ts =ts
        self.ms =ms
    def rutgon(self):
        a = math.gcd(self.ts,self.ms)
        self.ts//=a
        self.ms//=a
        return "{}/{}".format(self.ts,self.ms)
tu,mau = map(int,input().split())
ps = Phanso(tu,mau)
print(ps.rutgon())
