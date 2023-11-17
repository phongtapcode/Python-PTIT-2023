class Time:
    def __init__(self,id,name,timein,timeout):
        self.id = id
        self.name = name
        giovao,phutvao = map(int,timein.split(":"))
        giora,phutra = map(int,timeout.split(":"))
        if phutra-phutvao<0:
            self.phut = phutra+60-phutvao
            giovao+=1
        else:
            self.phut = phutra-phutvao
        if giora-giovao<0:
            self.gio = giora+24-giovao
        else:
            self.gio = giora-giovao
    def __str__(self):
        return f"{self.id} {self.name} {self.gio} gio {self.phut} phut"
a = []
for _ in range(int(input())):
    a.append(Time(input(),input(),input(),input()))
a.sort(key=lambda x: (-x.gio,-x.phut))
for i in a:
    print(i)
