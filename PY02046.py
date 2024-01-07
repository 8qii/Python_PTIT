import math

n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if i not in b:
        b.append(i)

tong = sum(b)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


tmp = 0
f = False
for i in range(0, len(b)):
    tmp += b[i]
    if is_prime(tmp) and is_prime(tong - tmp):
        print(i)
        f = True
        break

if not f:
    print("NOT FOUND")
