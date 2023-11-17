import math
cnt = 1
class Tn:
    def __init__(self,name,cu,moi,cnt):
        self.id = "TS0"+str(cnt)
        cnt+=1
        self.name = name
        if moi>10:
            moi/=10
        if cu>10:
            cu/=10
        self.diem = (moi+cu)/2
        if (moi+cu)/2>=9.5:
            self.notice = "XUAT SAC"
        elif (moi+cu)/2>=8:
            self.notice = "DAT"
        elif (moi+cu)/2>=5:
            self.notice = "CAN NHAC"
        else:
            self.notice = "TRUOT"
    def __str__(self):
        return self.id+" "+self.name+" "+"{:.2f}".format(self.diem)+" "+self.notice
a = []       
for _ in range(int(input())):
    a.append(Tn(input(),float(input()),float(input()),cnt))
    cnt+=1
a.sort(key= lambda x: -x.diem)
for i in a:
    print(i)