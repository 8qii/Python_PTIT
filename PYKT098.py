def check(s):
    if not s.isdigit():
        return True
    else:
        if 2147483647 >= int(s) >= -2147483648:
            return False
    return True


m = []
file = open('DATA.in', 'r')

for line in file:
    a = line.split()
    for i in a:
        if check(i):
            m.append(i)

m = sorted(m)
for i in m:
    print(i, end = ' ')