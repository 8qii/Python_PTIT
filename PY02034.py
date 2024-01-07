s = input()
if len(s) % 2 == 1:
    s = s[:-1]

m = {}
for i in range(0, len(s), 2):
    if int(s[i:i+2]) in m:
        m[int(s[i:i + 2])] += 1
    else: m[int(s[i:i+2])] = 1


for i in m:
    print(i, m[i])