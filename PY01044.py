a = input()
b = input()
c = a.lower().split()
d = b.lower().split()
hop = []
giao = []
for i in c:
    if i not in hop:
        hop.append(i)

for i in d:
    if i not in hop:
        hop.append(i)

for i in c:
    if i in d:
        if i not in giao:
            giao.append(i)

hop = sorted(hop)
giao = sorted(giao)
print(*hop)
print(*giao)
