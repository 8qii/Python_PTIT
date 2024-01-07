import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2


n = int(input())
a = list(int(i) for i in input().split())
dd = {}
for i in a:
    if isPrime(i):
        if i in dd:
            dd[i] += 1
        else :
            dd[i] = 1
for i in dd:
    if dd[i] > 0:
        print(str(i) + " " + str(dd[i]))