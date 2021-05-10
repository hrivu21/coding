def lis(l, index, memo):  # accepted

    if len(l) == 0:
        return 0

    if index in memo:
        return memo[index]

    if index == 0:
        memo[index] = 1
        return 1

    m = 0
    flag = False
    for i in range(index):
        n = lis(l, i, memo)
        if l[i] < l[index] and n > m:
            flag = True
            m = n
    if flag:
        to_return = 1 + m
    else:
        to_return = 1

    memo[index] = to_return
    return to_return


def lds(l, index, memo):  # accepted

    if len(l) == 0:
        return 0

    if index in memo:
        return memo[index]

    if index == len(l) - 1:
        memo[index] = 1
        return 1

    m = 0
    flag = False
    for i in range(index + 1, len(l)):
        n = lds(l, i, memo)
        if l[i] < l[index] and n > m:
            flag = True
            m = n
    if flag:
        to_return = 1 + m
    else:
        to_return = 1

    memo[index] = to_return
    return to_return


def longestiBtonicSeq(l):
    memo_i = dict()
    memo_d = dict()
    lis(l, len(l) - 1, memo_i)
    lds(l, 0, memo_d)

    m = 0
    for i in range(len(l)):
        m = max(m, memo_i[i] + memo_d[i] - 1)

    return m


# l = [10, 5, 2, 5, 7, 11, 6]
t = int(input())
for _ in range(t):
    input()
    l = list(map(int, input().split()))
    print(longestiBtonicSeq(l))
