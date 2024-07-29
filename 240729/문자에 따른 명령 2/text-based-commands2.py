instructions = input()
x, y = [0, 0]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0
for instruction in instructions:
    if instruction == "L":
        direction = (direction - 1) % 4
    elif instruction == "R":
        direction = (direction + 1) %4
    else:
        x, y = x + dx[direction], y + dy[direction]
    
print(x, end=" ")
print(y)