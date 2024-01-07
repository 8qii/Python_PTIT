s = input()
if len(s) % 2 == 1:
    s = s[:-1]

m = {}
for i in range(0, len(s), 2):
    m[s[i:i+2]] = 1

m = sorted(m.items(), key= lambda x : x[0])

for i in m:
    print(i[0], end = ' ')