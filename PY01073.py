s = input()
n = len(s)

a = [0] * n
vs = [0] * (n+5)

def gen(strr):
    if len(strr) == n:
        print(strr)
    for i in range (1,n + 1):
        if vs[i] == 0:
            vs[i] = 1
            gen(strr + s[i-1])
            vs[i] = 0

gen("")