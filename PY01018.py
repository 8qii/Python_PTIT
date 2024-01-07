p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    s = input()
    if s == '0':
        break
    n, s = s.split()
    n = int(n)
    res = ''
    for i in s:
        j = p.find(i)
        res += p[(j + n) % 28]
    print(res[::-1])