import math

class Phanso:
    def __init__(self,ts,ms):
        self.ts =ts
        self.ms =ms
    def rutgon(self,ps2):
        tuso = self.ts*ps2.ms+ps2.ts*self.ms
        mauso = self.ms*ps2.ms
        return "{}/{}".format(int(tuso/math.gcd(tuso,mauso)),int(mauso/math.gcd(tuso,mauso)))
tu1,mau1,tu2,mau2 = map(int,input().split())
ps1 = Phanso(tu1,mau1)
ps2 = Phanso(tu2,mau2)
print(ps1.rutgon(ps2))
