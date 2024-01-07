class tnv:

    def __init__(self, name, m1, m2, num):
        self.name = name
        if m1 > 10:
            m1 /= 10
        if m2 > 10:
            m2 /= 10
        self.avg = (m1 + m2) / 2
        self.id = "TS0" + "{:01d}".format(num)

    def xep_loai(self):
        if self.avg >= 9.5 : return "XUAT SAC"
        if self.avg >= 8: return "DAT"
        if self.avg >= 5: return "CAN NHAC"
        return "TRUOT"

    def output(self):
        print(self.id, self.name, "{:.2f}".format(self.avg), self.xep_loai())


k = int(input())
a = []
for t in range(k):
    x = tnv(input(), float(input()), float(input()), t + 1)
    a.append(x)

a = sorted(a, key = lambda x : (- x.avg))

for i in a:
    i.output()
