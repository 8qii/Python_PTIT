
class HoaDon:

    def __init__(self, name, dau, cuoi, stt):
        self.id = "KH" + "{:02d}".format(stt)
        self.name = name
        self.dau = dau
        self.cuoi = cuoi
        self.so = cuoi - dau

    def thanh_tien(self):
        if self.so <= 50:
            return round(100 * 1.02 * self.so)
        if self.so <= 100:
            return round((100 * 50 + 150 * (self.so - 50)) * 1.03)
        return round((100 * 50 + 150 * 50 + (self.so - 100) * 200) * 1.05)

    def output(self):
        print(str(self.id) + " " + str(self.name) + " " + str(self.thanh_tien()))

a = []
k = int(input())
for t in range (k):
    x = HoaDon(input(), int(input()), int(input()), t + 1)
    a.append(x)

a = sorted(a, key = lambda x : (-x.thanh_tien()))

for nguoi in a:
    nguoi.output()
