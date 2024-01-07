import math


def isPrime(s):
    k = int(s)
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return k > 1


for t in range(int(input())):
    n = input()
    cnt = 0
    for i in n:
        if isPrime(i):
            cnt += 1
        else:
            cnt -= 1

    if isPrime(len(n)) and cnt > 0:
        print("YES")
    else :
        print("NO")
