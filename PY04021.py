class PY04021:

    def __init__(self, id, name, tgian, on_time):
        self.id = id
        self.name = name
        self.tgian = tgian
        self.on_time = on_time

    def output(self):
        print(self.id + " " + self.name + " " + self.tgian)


if __name__ == '__main__':
    l = []
    for t in range(int(input())):
        id = input()
        name = input()
        di = input().split(':')
        den = input().split(':')
        on_time = (int(den[0]) - int(di[0])) * 60 + int(den[1]) - int(di[1])
        h = int(on_time // 60)
        m = int(on_time % 60)
        tgian = str(h) + " gio " + str(m) + " phut"
        x = PY04021(id, name, tgian, on_time)
        l.append(x)
    l = sorted(l, key=lambda x: -x.on_time)
    for x in l:
        x.output()
