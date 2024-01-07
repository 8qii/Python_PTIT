n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)
    if s == '':
        print(a[0], len(a) - 2, sep = ': ')
        a.clear()
        n += 1
print(a[0] + ':', len(a) - 1)