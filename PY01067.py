def check(ss):
    cnt = 0
    for i in ss:
        if i == '2':
            cnt += 1
    if cnt * 2 > len(ss):
        return True
    return False

a = []
b = ['0', '1', '2']

def gen(j):
    if check(j):
        a.append(j)
    if len(j) < 10:
        for i in b:
            gen(j + i)

gen('1')
gen('2')
a = sorted([int(i) for i in a])
t = int(input())
for q in range(t):
    n = int(input())
    for i in range(n):
        print(a[i], end = ' ')
    print()

