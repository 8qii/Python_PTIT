class dk:
    def __init__(self, ma, name, date, time):
        self.ma = ma
        self.name = name
        self.date = date
        self.time = time
        tmp = [int(i) for i in date.split('/')]
        self.ngay = tmp[0]
        self.thang = tmp[1]
        self.nam = tmp[2]
        self.id = 'T{:03d}'.format(num)

    def output(self):
        print(self.id + " " + self.ma + " " + self.name +
              " " + self.date + " " + self.time)


num = 1
n, k = [int(i) for i in input().split()]
l = []
a = []
for i in range(n*2):
    s = input()
    a.append(s)

for i in range(k):
    num = i+1
    s = input()
    tmp = s.split()
    ma = tmp[0]
    name = ''
    for f in range(2*n):
        if a[f] == ma:
            name = a[f+1]
            break
    date = tmp[1]
    time = tmp[2] + ' ' + tmp[3]
    x = dk(ma, name, date, time)
    l.append(x)

l = sorted(l, key=lambda x: (x.nam, x.thang, x.ngay, x.time))
for i in l:
    i.output()
