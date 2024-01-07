from datetime import *

class PY04016:

    def __init__(self, num, name, so, ngayo, phatsinh):
        self.id = 'KH{:02d}'.format(num)
        self.name = name
        self.so = so
        self.ngayo = ngayo
        self.phatsinh = phatsinh
        if self.so[0] == '1':
            self.gia = 25
        elif self.so[0] == '2':
            self.gia = 34
        elif self.so[0] == '3':
            self.gia = 50
        else: self.gia = 80

        self.thanhtien = int(self.ngayo * self.gia + self.phatsinh)

    def output(self):
        print(self.id, self.name, self.so, self.ngayo, self.thanhtien, sep = ' ')


a = []
for t in range(int(input())):
    id = t+1
    name = input()
    so = input()
    den = [int(i) for i in input().split('/')]
    di = [int(i) for i in input().split('/')]
    ngayden = date(den[2], den[1], den[0])
    ngaydi = date(di[2], di[1], di[0])
    ngayo = int((ngaydi - ngayden).total_seconds() // (24 * 3600) + 1)
    phatsinh = int(input())

    x = PY04016(id, name, so, ngayo, phatsinh)
    a.append(x)
a = sorted(a, key = lambda x : -x.thanhtien)
for i in a:
    i.output()
