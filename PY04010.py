

class PY04010:
    def __init__(self, name, dob, m1, m2, m3):
        self.name = name
        self.dob = dob
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.tong = m1 + m2 + m3

    def output(self):
        print(self.name + " " + self.dob + " " + "{:.1f}".format(self.tong))


if __name__ == '__main__':
    a = PY04010(input(), input(), float(input()), float(input()), float(input()))
    a.output()