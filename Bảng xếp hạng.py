class Submit:
    def __init__(self,name,ac,cntsubmit):
        self.ac=ac
        self.name=name
        self.cntsubmit=cntsubmit
    def __str__(self):
        return f"{self.name} {self.ac} {self.cntsubmit}"
sub = []
for t in range(int(input())):
    name = input()
    ac,cntsubmit = map(int,input().split())
    sub.append(Submit(name,ac,cntsubmit))
sub.sort(key= lambda x: (-x.ac,x.cntsubmit,x.name))
for i in sub:
    print(i)

