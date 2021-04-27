def f(l):
    l.sort()
    diff = 0
    for i in range(1, len(l)+1):
        if i < l[i-1]:
            return 0
        diff += i - l[i-1]
    return diff

try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        d = f(l)
        # print(d)
        if d%2 != 0:
            print('First')
        else:
            print('Second')

except:
    pass