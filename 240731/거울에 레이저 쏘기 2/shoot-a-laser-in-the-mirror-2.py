def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N


def get_start(k, n):
    if k <= n:
        x, y = 1, k
    elif n < k <= 2*n:
        x, y = k - n, n
    elif 2*n < k <= 3*n:
        x, y = n, 3*n - k + 1
    else:
        x, y = 4*n - k + 1, 1 

    return [x-1, y-1]


def turn(dir, str):
    ndir = None

    if str == "/":
        if dir == 0:
            ndir = 1
        elif dir == 1:
            ndir = 0
        elif dir == 2:
            ndir = 3
        else:
            ndir = 2
    else:
        if dir == 0:
            ndir = 3
        elif dir == 1:
            ndir = 2
        elif dir == 2:
            ndir = 1
        else:
            ndir = 0

    return ndir


def reflect(x, y, dir):
    # print(x, y, dir)
    ndir = turn(dir, table[x][y])
    # print(f"ndir: {ndir}")

    nx = x + dxs[ndir]
    ny = y + dys[ndir]

    return [nx, ny, ndir]


if __name__ == "__main__":
    N = int(input())

    input_list = []
    table = []
    for _ in range(N):
        input_list.append(input())
    for string in input_list:
        table.append(list(string))

    K = int(input())

    directions = {
        "N": 0,
        "E": 1,
        "S": 2,
        "W": 3
    }

    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]

    start = get_start(K, N)
    x, y = start
    dir = (K - 1) // 4
    
    count = 0
    while in_range(x, y, N):
        nx, ny, ndir = reflect(x, y, dir)
        count += 1
        
        x, y, dir = nx, ny, ndir
        

    print(count)