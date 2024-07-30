def move(dir, x, y):
    nx = x + dx[dir]
    ny = y + dy[dir]

    return [nx, ny]

instructions = input()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# North
dir = 0
x, y = 0, 0
count = 0

for idx, instruction in enumerate(instructions):
    count += 1
    if instruction == "R":
        dir = (dir + 1) % 4
    elif instruction == "L":
        dir = (dir - 1) % 4
    else:
        nx, ny = move(dir, x, y)

    if nx == 0 and ny == 0:
        print(count)
        break
    elif idx == len(instructions) - 1:
        print(-1)

    x, y = nx, ny