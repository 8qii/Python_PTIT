for t in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    b = []
    for i in lst:
        b.append(sum(int(j) for j in str(i)))

    for i in range (len(lst) - 1):
        for j in range (i + 1 , len(lst)):
            if b[i] == b[j]:
                if lst[i] > lst[j]:
                    tmp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = tmp

                    tmp = b[i]
                    b[i] = b[j]
                    b[j] = tmp

            if b[i] > b[j] :
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp

                tmp = b[i]
                b[i] = b[j]
                b[j] = tmp

    print(*lst)