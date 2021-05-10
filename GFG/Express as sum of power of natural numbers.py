
def express(k, n, i, memo):
    key = n, i
    if key in memo:
        return memo[key]

    x = i**k
    if x == n:
        to_return = 1

    elif x < n:
        to_return = express(k, n - x, i + 1, memo) + express(k, n, i + 1, memo)

    else:
        to_return = 0

    memo[key] = to_return
    return to_return


t = int(input())
for _ in range(t):
    n, k = tuple(map(int, input().split()))
    memo = dict()
    print(express(k, n, 1, memo))
