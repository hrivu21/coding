def is_in_grid(i, j):
    return i >= 0 and i < r and j >= 0 and j < c


def is_Wolf_adjacent(i, j):
    return (i-1) >= 0 and grid[i-1][j] == 'W' or \
        (i+1) < r and grid[i+1][j] == 'W' or \
        (j-1) >= 0 and grid[i][j-1] == 'W' or \
        (j+1) < c and grid[i][j+1] == 'W'


def floodfill(grid, i, j, visited):  # -> bool
    if (i, j) in visited:
        return True

    visited.add((i, j))

    if is_Wolf_adjacent(i, j):
        return False

    else:
        w = x = y = z = True

        if is_in_grid(i+1, j):
            if grid[i+1][j] == 'S':
                w = floodfill(grid, i+1, j, visited)
            else:
                grid[i+1][j] = 'D'

        if is_in_grid(i-1, j):
            if grid[i-1][j] == 'S':
                x = floodfill(grid, i-1, j, visited)
            else:
                grid[i-1][j] = 'D'

        if is_in_grid(i, j+1):
            if grid[i][j+1] == 'S':
                y = floodfill(grid, i, j+1, visited)
            else:
                grid[i][j+1] = 'D'

        if is_in_grid(i, j-1):
            if grid[i][j-1] == 'S':
                z = floodfill(grid, i, j-1, visited)
            else:
                grid[i][j-1] = 'D'

    return w and x and y and z


def is_protectable(grid):		# -> bool
    visited = set()

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'S' and (i, j) not in visited:
                z = floodfill(grid, i, j, visited)
                if not z:
                    return False
    return True


if __name__ == '__main__':
    # global r
    # global c
    r, c = tuple(map(int, input().split()))
    grid = []
    for i in range(r):
        x = list(input())
        grid.append(x)

    res = is_protectable(grid)
    d = {True: 'Yes', False: 'No'}

    print(d[res])
    if res:
        for i in range(r):
            print(''.join(map(str, grid[i])))
