from collections import defaultdict


def find_reachable_leaves(tree, node=1, consequtive=0, parent=-1):
    # visited.add(node)

    if a[node-1] == 1:
        consequtive += 1
        if consequtive == m+1:
            return 0
    else:
        consequtive = 0

    is_leaf = True
    reachable_leaves_count = 0

    for child in tree[node]:
        if child != parent:
            is_leaf = False
            reachable_leaves_count += find_reachable_leaves(tree, child, consequtive, node)

    if is_leaf:
        reachable_leaves_count = 1

    return reachable_leaves_count


if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))

    tree = defaultdict(list)

    for i in range(n - 1):
        x, y = tuple(map(int, input().split()))
        tree[x].append(y)
        tree[y].append(x)

    # print(tree)

    res = find_reachable_leaves(tree)

    print(res)
