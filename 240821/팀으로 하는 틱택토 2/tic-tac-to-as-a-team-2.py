def init():
    global grid
    global participants

    for _ in range(3):
        _input = [int(num) for num in input()]
        grid.append(_input)

        for element in _input:
            participants.add(int(element))


def play_game(grid, participants):
    count = 0
    participants_list = list(participants)

    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            team = [participants_list[i], participants_list[j]]

            # horizontal
            for row in grid:
                if all(elem in team for elem in row) and len(set(row)) > 1:
                    count += 1

            # vertical
            for col in range(3):
                vertical_row = [grid[0][col], grid[1][col], grid[2][col]]
                if all(elem in team for elem in vertical_row) and len(set(vertical_row)) > 1:
                    count += 1

            # diagonal(2 cases)
            main_diagonal = [grid[k][k] for k in range(3)]
            if all(elem in team for elem in main_diagonal) and len(set(main_diagonal)) > 1:
                count += 1
            anti_diagonal = [grid[k][2 - k] for k in range(3)]
            if all(elem in team for elem in anti_diagonal) and len(set(anti_diagonal)) > 1:
                count += 1

    return count


if __name__ == "__main__":
    grid = []
    participants = set()

    init()
    print(play_game(grid, participants))