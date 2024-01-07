m = {}
s = 0

file = open('VANBAN.in', 'r')

for x in file:
    a = x.split()
    for i in a:
        if i == i[::-1]:
            if len(i) > s:
                s = len(i)
                m.clear()
                m[i] = 1
            elif len(i) == s:
                if i not in m:
                    m[i] = 1
                else:
                    m[i] += 1

for i in m:
    print(i, m[i], sep = ' ')