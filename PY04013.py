
static_id = 0

class ttlm:

    def __init__(self, name):
        self.id = "T" + "{:02d}".format(static_id)
        self.name = name
        self.total_time = 0
        self.total_amount = 0

    def add(self, start, end, amount):
        self.total_time += -int(start[:2]) * 60 - int(start[3:]) + int(end[:2]) * 60 + int(end[3:])
        self.total_amount += amount

    def to_hour(self):
        return self.total_time / 60

    def get_avg(self):
        return "{:.2f}".format(self.total_amount / self.to_hour())

    def output(self):
        print(str(self.id) + " " + str(self.name) + " " + self.get_avg())


if __name__ == '__main__':
    a = []
    for t in range(int(input())):
        n = input()
        s = input()
        e = input()
        am = int(input())
        done = False
        for tram in a:
            if tram.name == n:
                done = True
                tram.add(s, e, am)
                break

        if not done :
            static_id += 1
            x = ttlm(n)
            x.add(s, e, am)
            a.append(x)

    for tram in a:
        tram.output()