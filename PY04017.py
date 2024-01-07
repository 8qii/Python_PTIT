class PY04017:
    def __init__(self, name, prov, runtime):
        self.name = name
        self.prov = prov
        id = ""
        tmp = prov.split()
        for i in tmp:
            id += i[0]
        tmp = name.split()
        for i in tmp:
            id += i[0]
        self.id = id.upper()
        self.speed = round(120/runtime)

    def output(self):
        print(self.id, self.name, self.prov, self.speed, "Km/h", sep=' ')


a = []
for t in range(int(input())):
    name = input()
    prov = input()
    fin = [int(i) for i in input().split(':')]
    runtime = fin[0] - 6 + (fin[1] / 60)
    x = PY04017(name, prov, runtime)
    a.append(x)

a = sorted(a, key=lambda x: -x.speed)
for i in a:
    i.output()
