from collections import defaultdict

try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        w = input().split()

        d = defaultdict(set)
        for i in range(len(w)):
            d[w[i][0]].add(w[i][1:])

        keys = tuple(d.keys())

        res = 0
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                x = d[keys[i]].difference(d[keys[j]])
                y = d[keys[j]].difference(d[keys[i]])

                res += len(x) * len(y)

        print(2 * res)

except Exception as e:
    print(e)