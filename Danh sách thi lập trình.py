cnt = 1
class TS:
    def __init__(self,name,team,cnt):
        if cnt<10:
            self.id = "C00"+str(cnt)
        elif cnt>=10 and cnt<100:
            self.id = "C0"+str(cnt)
        else:
            self.id = "C"+str(cnt)
        self.name = name
        self.team = int(team[4:])
    def __str__(self):
        return self.id + " " +self.name 
t = int(input())
sodoi = []
for _ in range(t):
    sodoi.append(input()+" "+input())
arr = []
for _ in range(int(input())):
    arr.append(TS(input(),input(),cnt))
    cnt+=1
arr.sort(key = lambda x: x.name)
for i in arr:
    print(i,end=" ")
    print(sodoi[i.team-1])