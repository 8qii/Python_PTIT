n =int(input())
a = [float(i) for i in input().split()]

mi = min(a)
ma = max(a)

res = []
for i in a:
    if i != mi and i != ma:
        res.append(i)

print("{:.2f}".format(sum(res) / len(res)))