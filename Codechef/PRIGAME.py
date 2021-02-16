def isPrime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


try:
    # file1 = open("pr.txt", "w")
    # file1.write("0, 0, ")
    # n = 10 ** 6
    # count = 0
    # p = [0, 0]
    # for i in range(2, n + 1):
    #     if isPrime(i):
    #         count += 1
    #     p.append(count)
    # file1.write(str(p[-1]) + ", ")
    # print(p)

    t = int(input())
    X = list()
    Y = list()
    for _ in range(t):
        x, y = tuple(map(int, input().split()))
        X.append(x)
        Y.append(y)

    n = max(X)
    count = 0
    p = [0, 0]
    for i in range(2, n + 1):
        if isPrime(i):
            count += 1
        p.append(count)

    for i in range(t):
        x, y = X[i], Y[i]
        if p[x] > y:
            print("Divyam")
        else:
            print("Chef")

except Exception as e:
    pass