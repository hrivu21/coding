from math import ceil

t = int(input())

for i in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    l = list(map(int, input().split()))

    hits = 0
    pos_prev = w.index(1)

    for j in range(2, n + 1):

        if w.index(j) > pos_prev:
            pos_prev = w.index(j)
            continue

        else:
            hit = ceil((pos_prev - w.index(j) + 1) / l[w.index(j)])
            pos_prev = w.index(j) + l[w.index(j)] * hit
            hits += hit

    print(hits)
