# def in_range(x, y, n):
#     return 0<=x<n and 0<=y<n

def move(dir, x, y):
    nx = x + dx[dir]
    ny = y + dy[dir]

    return [nx, ny]


N = int(input())
instructions = []

for _ in range(N):
    dir, dist = input().split()

    instructions.append([dir, int(dist)])

directions = {
    "N": 0,
    "E": 1,
    "S": 2,
    "W": 3

}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = [0, 0]
count = 0
is_back = False

for instruction in instructions:
    dir = directions[instruction[0]]
    dist = instruction[1]
    
    for i in range(dist):
        count += 1
        nx, ny = move(dir, x, y)

        if nx == 0 and ny == 0:
            print(count)
            is_back = True
            break

        x, y = nx, ny

    if is_back:
        break
        
    N -= 1
    if N == 0:
        print(-1)
        break