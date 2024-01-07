class PY04012:
    def __init__(self, id, name, lop):
        self.id = id
        self.name = name
        self.lop = lop
        self.diemdanh = None


    def set_diem_danh(self, s):
        self.diemdanh = s

    def tinhdiem(self):
        s = self.diemdanh
        diem = 10
        for i in s:
            if i == 'm': diem -= 1
            elif i == 'v': diem -= 2

        if diem <= 0:
            diem = 0
            return "0 KDDK"
        else: return str(diem)

    def output(self):
        print(self.id, self.name, self.lop, self.tinhdiem(), sep = ' ')


if __name__ == '__main__':
    n = int(input())
    a = []
    for t in range(n):
        x = PY04012(input(), input(), input())
        a.append(x)

    for t in range(n):
        tmp = input().split()
        for j in a:
            if j.id == tmp[0]:
                j.set_diem_danh(tmp[1])
                break

    for i in a:
        i.output()