import math
cnt = 1
class Tn:
    def __init__(self,name,cu,moi,cnt):
        if cnt<10:
            self.id = "KH0"+str(cnt)
        else:
            self.id = "KH"+str(cnt)
        cnt+=1
        self.name = name
        a = moi-cu
        if a<=50:
            self.tien = (a)*100+((a*100)*2)/100
        elif a<=100:
            tmp = 50*100 + (a-50)*150
            self.tien = tmp*103.0/100
        else:
            tmp = 50*250 + (a-100)*200
            self.tien = tmp*105.0/100
    def __str__(self):
        return self.id+" "+self.name+" "+"{:.0f}".format(self.tien)
a = []       
for _ in range(int(input())):
    a.append(Tn(input(),float(input()),float(input()),cnt))
    cnt+=1
a.sort(key= lambda x: -x.tien)
for i in a:
    print(i)