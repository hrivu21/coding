# AC
from math import log2


def func(x):
    t = 0
    task = 1
    l = []
    while not log2(x+1) == int(log2(x+1)):
        # print(x)
        if task == 1:
            m = len(bin(x))-2
            x ^= 2**(m)-1
            l.append(m)
        else:
            x += 1
        task ^= 1
        t += 1
    print(t)
    print(*l)


if __name__ == '__main__':
    x = int(input())

    func(x)
