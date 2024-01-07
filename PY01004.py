import cmath


def isprime(n):
    if n < 2:
        return 0
    for i in range(2, cmath.sqrt(n)):
        if n % i == 0:
            return 0
    return 1


for i in range(0, int(input())):
    k = int(input())
    if isprime(k) == 1:
        print("YES")
    else:
        print("NO")
