import math


def is_prime(num):
    if num < 2: return False
    for i in range(2, round(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
m = {}
for i in a:
    if i not in m:
        m[i] = 1

a = list(m)
s = sum(a)
tmp = 0
found = False
for i in range(len(a)):
    tmp += a[i]
    if is_prime(tmp) and is_prime(s - tmp):
        found = True
        print(i)
        break
if not found:
    print("NOT FOUND")
