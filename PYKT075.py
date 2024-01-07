class PYKT075:
    def __init__(self, date, name, sdt):
        self.date = date
        self.name = name
        self.sdt = sdt
        k = name.split()
        if len(k) >= 1:
            self.ten = name.split(' ')[-1]
        else:
            self.ten = self.name

    def output(self):
        return self.name + ": " + self.sdt + " " + self.date + '\n'


file = open('SOTAY.txt', 'r')
arr = file.read().split('\n')
a = []
ngay = ''
while len(arr) > 0:
    tmp = arr[0]
    arr.pop(0)
    if tmp[:4] == 'Ngay':
        ngay = tmp[5:]
    elif len(arr) > 0:
        sdt = arr[0]
        arr.pop(0)
        a.append(PYKT075(ngay, tmp, sdt))

a = sorted(a, key=lambda x: (x.ten, x.name))
file.close()
ghi = open('DIENTHOAI.txt', 'w')
for i in a:
    ghi.write(i.output())
ghi.close()
