def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N


def get_start(k, n):
    x, y, dir = 0, 0, 0
    
    if k <= n:
        x, y = 0, k - 1
        dir = 0
    elif n < k <= 2*n:
        x, y = k - n - 1, n - 1
        dir = 1
    elif 2*n < k <= 3*n:
        x, y = n - 1, 3*n - k
        dir = 2
    else:
        x, y = 4*n - k, 0 
        dir = 3

    return [x, y, dir]


def turn(dir, char):
    ndir = None

    if char == "/":
        return [1,0,3,2][dir]
    else:
        return [3,2,1,0][dir]


def reflect(x, y, dir):
    ndir = turn(dir, table[x][y])
    nx = x + dxs[ndir]
    ny = y + dys[ndir]

    return [nx, ny, ndir]


if __name__ == "__main__":
    N = int(input())
    table = [list(input()) for _ in range(N)]
    K = int(input())

    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]

    x, y, dir = get_start(K, N)
    count = 0

    while in_range(x, y, N):
        nx, ny, ndir = reflect(x, y, dir)
        count += 1
        
        x, y, dir = nx, ny, ndir
        

    print(count)