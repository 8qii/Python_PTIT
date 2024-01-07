import math


def isPrime(n):
    if n < 2 :
        return False
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def getSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum

for _ in range (int(input())):
    s = input().split()
    a , b = [int(i) for i in s]
    c = math.gcd(a,b)
    if isPrime(sum(int(i) for i in str(math.gcd(a, b)))) :
        print("YES")
    else:
        print("NO")

