def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N


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

    # print(nx, ny)


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

    x, y = [(K - 1) // 4, ((K) % 4) - 1]
    dir = (K - 1) // 4
    
    count = 0
    while in_range(x, y, N):
        nx, ny, ndir = reflect(x, y, dir)
        count += 1
        
        x, y, dir = nx, ny, ndir
        

    print(count)