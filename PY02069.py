def tn(s):
    if s == s[::-1] and len(s) > 1:
        return True
    return False


n, k = [int(i) for i in input().split()]
a = [0] * n
for p in range(n):
    a[p] = [int(i) for i in input().split()]

m = {}
val = -1
for i in range(n):
    for j in range(k):
        if tn(str(a[i][j])):
            if a[i][j] > val:
                val = a[i][j]

if val == -1:
    print('NOT FOUND')
else:
    print(val)
    for i in range(n):
        for j in range(k):
            if a[i][j] == val:
                print('Vi tri [' + str(i) + '][' + str(j) + ']')
