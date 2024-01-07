import math


def isPrime(n):
    if n < 2:
        return "NO"
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 'NO'

    return 'YES'

for t in range (int(input())):
    tong = 0
    tong = sum(int(i) for i in input())
    print(isPrime(tong))
