def explode_and_gravity(bombs, m):
    n = len(bombs)
    marked = [False] * n

    i = 0
    while i < n:
        j = i
        while j < n and bombs[j] == bombs[i]:
            j += 1
        if j - i >= m:
            for k in range(i, j):
                marked[k] = True
        i = j

    return [bombs[k] for k in range(n) if not marked[k]]


if __name__ == "__main__":
    n, m = map(int, input().split())
    bombs = [int(input()) for _ in range(n)]

    while True:
        new_bombs = explode_and_gravity(bombs, m)
        if new_bombs == bombs:
            break
        bombs = new_bombs

    print(len(bombs))
    for bomb in bombs:
        print(bomb)
