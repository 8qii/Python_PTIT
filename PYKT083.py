m = {}

def calc(arr):
    if arr[3] == 'OUT': return 0
    if arr[1] == "Xe_con":
        if arr[2] == "5": return 10000
        if arr[2] == "7": return 15000
    if arr[1] == "Xe_tai": return 20000
    if arr[1] == "Xe_khach":
        if arr[2] == "29": return 50000
    return 70000


for t in range(int(input())):
    a = input().split()
    if a[4] in m:
        m[a[4]] += calc(a)
    else:
        m[a[4]] = calc(a)

m = sorted(m.items(), key= lambda x : x[0])
for i in m:
    print(i[0], i[1], sep = ': ')

