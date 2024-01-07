n = int(input())
a = [int(i) for i in input().split()]
ok = True
while ok:
    ok = False
    i = 0
    while i < len(a) - 1:
        if (a[i] + a[i+1]) % 2 == 0:
            a.pop(i)
            a.pop(i)
            ok = True
        i += 1

print(len(a))
