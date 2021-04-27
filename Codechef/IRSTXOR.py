def f(c):
    c = bin(c)[2:]
    a = '1'
    b = '0'

    for i in range(1, len(c)):
        if c[i] == '0':
            a += '1'
            b += '1'
        else:
            a += '0'
            b += '1'


    return int(a, 2) * int(b, 2)

try:
    t = int(input())
    for _ in range(t):
        c = int(input())
        print(f(c))
    
except:
    pass
