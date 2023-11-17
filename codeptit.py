class MonThi:
    def __init__(self, ma, ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc

    def __str__(self):
        return f"{self.ma} {self.ten} {self.hinhthuc}"

    def get_ma(self):
        return self.ma

def main():
    try:
        with open("MONHOC.in", "r") as file:
            n = int(file.readline().strip())
            a = [MonThi(file.readline().strip(), file.readline().strip(), file.readline().strip()) for _ in range(n)]
        
        a.sort(key=lambda x: x.get_ma())

        for x in a:
            print(x)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
