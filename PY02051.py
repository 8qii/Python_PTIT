n = int(input())
sl = []
s = 0
for t in range(n):
    b = [int(i) for i in input().split()]
    s += sum(b)
    sl.append(sum(b))

s = s / 2 / (n - 1)

if n == 2 :
    for i in sl :
        print(int(i / 2), end = ' ')
else:
    for i in range(n):
        print(int((sl[i] - s) / (n - 2)), end = ' ')
