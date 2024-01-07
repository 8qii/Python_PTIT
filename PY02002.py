f = [1] * 95
for i in range (3,95):
    f[i] = f[i-1] + f[i-2]

for t in range(int(input())):
    a,b = (int(i) for i in input().split())
    for k in range (a, b + 1):
        print(f[k] , end = ' ')

    print()