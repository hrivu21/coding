def subset(l, i, target, memo):
    key = i, target
    if key in memo:
        return memo[key]

    if target == 0:
        return True
    if target < 0 or i == -1:
        return False

    to_return = subset(l, i-1, target-l[i], memo) or subset(l, i-1, target, memo)
    memo[key] = to_return
    return to_return


t = int(input())
for _ in range(t):
    d = {True: 'YES', False: 'NO'}
    input()
    l = list(map(int, input().split()))
    memo = dict()
    target = sum(l)
    if target % 2 != 0:
        print('NO')

    else:
        print(d[subset(l, len(l)-1, target/2, memo)])
