def f(l):
    m = abs(l[0] - l[-1])
    x = abs(l[1] - l[0]) + abs(l[1] - l[-1])
    y = abs(l[-2] - l[0]) + abs(l[-2] - l[-1])
    m += max(x, y)
    return m


try:
    t = int(input())
    for i in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        l.sort()
        print(f(l))
except:
    pass
    