N = 10 ** 18

l = []

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            l.append(i * j * k)
            k *= 5
        j *= 3
    i *= 2

l.sort()
m = {}
stt = 1
for i in range(len(l)):
    m[l[i]] = stt
    stt += 1

for t in range (int(input())):
    n = int(input())
    if n not in m:
        print('Not in sequence')
    else :
        print(m[n])