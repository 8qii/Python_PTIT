import math


def check(a, b):
    a, b = int(a), int(b)
    a = math.gcd(a, b)
    if a == 1:
        return "YES"
    return "NO"


for _ in range(int(input())):
    s = input()
    ss = s[::-1]
    print(check(s, ss))
