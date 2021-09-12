# l = [i for i in range(0, 10, 2)]

# print(", ".join(map(str, l)))


# for idx, num in enumerate(l):
#     print(idx, num)


def f(l):
    l[0] = 4
    return


l = [1, 2, 3, 4, 5]
f(l)
print(l)
