# def mulmodulo(a, b, m):
#     res = 0
#     for i in range(b):
#         res = (res + a) % m
#         print(i, res)
#     return res


def expmodulo(b, e, m):
    if e == 0:
        return 1
    res = 1
    for i in range(e):
        res *= b
        res %= m
    return res


def main():
    l = list(input())
    l.reverse()
    sum = 0
    for i in range(len(l)):
        if l[i] == '1':
            sum += expmodulo(2, i, 3)
    if sum % 3 == 0:
        return(1)
    else:
        return(0)


t = int(input())
for _ in range(t):
    print(main())
