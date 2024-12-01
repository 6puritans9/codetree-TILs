from collections import deque

class Grid():
    def __init__(self, data, n):
        self.data = data
        self.length = n


    def blast(self, grid, row_idx, start, end):
        for i in range(start, end):
            grid[row_idx][i] = 0


    def detonate(self, m):
        temp_grid = self.rotate("left", self.data)

        for row_idx, row in enumerate(temp_grid):
            i = 0
            count = 1
            # j = i

            while i < self.length - 1:
                if row[i] == row[i + 1]:
                    count += 1
                    # j += 1

                else:
                    if count >= m:
                        self.blast(temp_grid, row_idx, i - count + 1, i + 1)
                        count = 1

                i += 1

            if count >= m:
                self.blast(temp_grid, row_idx, i - count + 1, i + 1)

        self.data = self.rotate("right", temp_grid)


    # def gravity(self, grid):
    #     def fill(grid, col, values):
    #         for i in range(self.length -1, -1, -1):
    #             if len(values):
    #                 grid[i][col] = values.pop()
    #             else:
    #                 grid[i][col] = 0
    #
    #
    #     for x in range(self.length):
    #         values = deque()
    #
    #         for y in range(self.length):
    #             if grid[y][x]:
    #                 values.append(grid[y][x])
    #
    #         fill(grid, x, values)
    #
    #     self.data = grid

    def gravity(self, grid):
        for col in range(self.length):
            queue = deque([grid[row][col] for row in range(self.length) if grid[row][col]])

            for row in range(self.length - 1, -1, -1):
                grid[row][col] = queue.pop() if queue else 0


    def rotate(self, direction, grid=None):
        if grid is None:
            grid = self.data

        rotated = []
        if direction == "left":
            for x in range(self.length - 1, -1, -1):
                temp = []
                for y in range(self.length):
                    temp.append(grid[y][x])
                rotated.append(temp)
        else:
            for x in range(self.length):
                temp = []
                for y in range(self.length - 1, -1, -1):
                    temp.append(grid[y][x])
                rotated.append(temp)

            self.gravity(rotated)

        return rotated


if __name__ == "__main__":
    n, m, k = tuple(map(int, input().split()))
    data = [[int(num) for num in input().split()] for _ in range(n)]
    grid = Grid(data, n)

    for _ in range(k):
        grid.detonate(m)
        grid.data = grid.rotate("right")

    grid.detonate(m)

    count = 0
    for row in grid.data:
        for el in row:
            count += 1 if el else 0

    print(count)

