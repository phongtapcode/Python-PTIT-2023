class Infor:
    def __init__(self,name,ns,d1,d2,d3):
        self.name = name
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def result(self):
        return f"{self.name} {self.ns} "+"{:.1f}".format(self.d1+self.d2+self.d3)
people = Infor(input(),input(),float(input()),float(input()),float(input()))
print(people.result())