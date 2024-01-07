n, k = [int(i) for i in input().split()]
era = [True] * 10000
era[0] = False
era[1] = False
for i in range (2,10000):
    if era[i]:
        for j in range (2 * i , 10000 , i):
            era[j] = False

a = []
for i in range (2, 10000):
    if era[i]:
        a.append(i)

print(k , end = ' ')
for i in range(n):
    k += a[i]
    print(k, end = ' ')