def f(l):       # call by reference
    l.append(0)
    return


def f1(i):  # call by value
    i += 1
    return


l = [1, 2, 3, 4]
i = 0

f(l)
f1(i)

print(*l)
print(i)
