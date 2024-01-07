for t in range (int(input())):
    n = int(input())
    ar = []
    du = 0
    while n > 0:
        k = n % 10
        k += du
        n /= 10
        if k >= 5:
            k = 0
            du = 1
        else:
            k = 0
            du = 0
        ar.append(k)
    for i in range( len(ar) - 1 , 0 ):
        print(ar[i] , end = '')

