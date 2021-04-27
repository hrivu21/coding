def recur(N, E, H, price):
    if E < 0 or H < 0:
        return -1

    if N == 0:
        return 0

    for i in range(3):
        c = price[i][1]

        if price[i][0] == "omlette":
            x = recur(N - 1, E - 2, H, price)
        elif price[i][0] == "milkshake":
            x = recur(N - 1, E, H - 3, price)
        else:
            x = recur(N - 1, E - 1, H - 1, price)

        if x != -1:
            return c + x

    return -1


# N, E, H, A, B, C = 5, 4, 4, 2, 2, 2
# N, E, H, A, B, C = 4, 5, 5, 1, 2, 3
# N, E, H, A, B, C = 4, 5, 5, 3, 2, 1

try:
    t = int(input())
    for _ in range(t):
        N, E, H, A, B, C = tuple(map(int, input().split()))
        price = [("omlette", A), ("milkshake", B), ("cake", C)]
        price.sort(key=lambda x: x[1])

        print(recur(N, E, H, price))

except:
    pass
