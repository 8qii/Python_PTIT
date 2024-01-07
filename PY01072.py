n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [0] * (k + 1)
c = []
for i in a:
    if i not in c:
        c.append(i)


c.sort()
n = len(c)

def gen(j):
    if j == k:
        for i in range (1, k + 1):
            print(c[b[i] - 1] , end = ' ')
        print()
        return
    for i in range (b[j] + 1 , n + 1):
        b[j+1] = i
        gen(j+1)

gen(0)