from collections import defaultdict
import random


def f(N, L):
    
    mod = 998244353
    resSum = 0
    d = defaultdict(list)
    d[1] = [L[-1]]

    for i in range(N - 2, -1, -1):

        for prevlength in range(M, 1, -1):
            d[prevlength].extend(list(map(lambda x: x ^ L[i], d[prevlength - 1])))

        d[1].append(L[i])

    for key in d.keys():
        for x in d[key]:
            resSum = (resSum + x) % mod
        # resSum += sum(d[key]) % mod

    return resSum % mod


try:
    N = int(input())
    L = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        M = int(input())
        print(f(N, L, M))

except Exception as e:
    print(e)

# N = random.randrange(10 ** 2, 2 * 10 ** 2)
# L = list()
# for _ in range(N):
#     L.append(random.randrange(1, 2 ** 30))
# M = N
# print(N)
# print("Start")


# print(f(N, L, M))