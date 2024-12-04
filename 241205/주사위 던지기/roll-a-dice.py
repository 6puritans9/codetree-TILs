class Dice():
    def __init__(self):
        self.top = 1
        self.bottom = 6
        self.left = 4
        self.right = 3
        self.front = 2
        self.back = 5
    

    def roll(self, instruction):
        if instruction == "L":
            new_top = self.right
            new_bottom = self.left
            new_left = self.top
            new_right = self.bottom

            self.top = new_top
            self.bottom = new_bottom
            self.left = new_left
            self.right = new_right
        
        elif instruction == "R":
            new_top = self.left
            new_bottom = self.right
            new_left = self.bottom
            new_right = self.top

            self.top = new_top
            self.bottom = new_bottom
            self.left = new_left
            self.right = new_right

        elif instruction == "U":
            new_top = self.front
            new_bottom = self.back
            new_front = self.bottom
            new_back = self.top

            self.top = new_top
            self.bottom = new_bottom
            self.front = new_front
            self.back = new_back

        else:
            new_top = self.back
            new_bottom = self.front
            new_front = self.top
            new_back = self.bottom

            self.top = new_top
            self.bottom = new_bottom
            self.front = new_front
            self.back = new_back


def in_range(y, x, n):
    return 0<= y < n and 0<= x < n


def mark(grid, y, x, value):
        grid[y][x] = value


if __name__ == "__main__":
    n, m, r, c = tuple(map(int, input().split()))
    instructions = input().split()

    grid = [[0 for _ in range(n)] for _ in range(n)]
    directions = {"L":(0, -1), "R":(0, 1), "U": (-1, 0), "D": (1, 0)}
    dice = Dice()

    y, x = r-1, c-1
    mark(grid, y, x, dice.bottom)

    for instruction in instructions:
        dy, dx = directions[instruction]
        ny, nx = y + dy, x + dx

        if in_range(ny, nx, n):
            dice.roll(instruction)
            mark(grid, ny, nx, dice.bottom)
        y, x = ny, nx

    _sum = sum(sum(row) for row in grid)
    print(_sum)