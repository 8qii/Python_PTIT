import math


class sv:
    def __init__(self, name, tb):
        self.id = 'SV{:02d}'.format(num)
        self.name = self.name_format(name)
        self.tbb = '{:.2f}'.format(tb)
        self.tb = tb

    def name_format(self, name):
        tmp = name.lower().strip().split()
        for i in range(len(tmp)):
            tmp[i] = tmp[i][:1].upper() + tmp[i][1:]
        return ' '.join(tmp)

    def output(self):
        print(self.id + " " + self.name + " " + self.tbb + " ", end='')


num = 0
l = []
for t in range(int(input())):
    num = t + 1
    name = input()
    tb = (int(input()) * 3 + int(input()) * 3 + int(input()) * 2) / 8
    tb = math.ceil(tb * 100) / 100
    l.append(sv(name, tb))


l = sorted(l, key=lambda x: (-x.tb, x.id))

xh = 1
truoc = 1
diemtruoc = 10
for i in range(len(l)):
    l[i].output()
    if l[i].tb == diemtruoc:
        print(truoc)
    else:
        truoc = xh
        diemtruoc = l[i].tb
        print(xh)
    xh += 1
