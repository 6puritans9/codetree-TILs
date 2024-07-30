def in_range(x, y, n):
    return x>0 and x<n or y>0 and y<n

def turn(dir):
    return (3 - dir)

def move(dir, x, y):
    nx = x + dx[dir]
    ny = y + dy[dir]

    return [nx, ny]

n, t = [int(num) for num in input().split()]
r, c, d = input().split()
x, y = int(r) - 1, int(c) - 1

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

direction = {
    "U": 1,
    "R": 3,
    "L": 0,
    "D": 2
    }
dir = direction[d]
is_turning = False

while t:
    if not in_range(x, y, n) and not is_turning:
        dir = turn(dir)
        is_turning = True
    else:
        if is_turning:
            is_turning = False

        x, y = move(dir, x, y)

    t -= 1

print(x + 1, y + 1, end=" ")