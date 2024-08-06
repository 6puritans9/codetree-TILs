def in_range(x, y):
    LIMIT = 19

    return 0 <= x < LIMIT and 0 <= y < LIMIT


def check_status(table):
    # Helper Functions
    def check_hor(x, y, self_color):
        for i in range(1, 5):
            if table[x+i][y] != self_color:
                return False
            
        return True
        

    def check_ver(x, y, self_color):
        for i in range(1, 5):
            if table[x][y+i] != self_color:
                return False
            
        return True


    def check_dia_right(x, y, self_color):
        for i in range(1, 5):
            if table[x+i][y+i] != self_color:
                return False

        return True

    
    def check_dia_left(x, y, self_color):
        if not in_range(x, y-5):
            return False

        for i in range(1, 5):
            if table[x+i][y-i] != self_color:
                return False

        return True

    def does_win(x, y):
        self_color = table[x][y]
        if in_range(x+5, y+5) and check_hor(x, y, self_color) or check_ver(x,y, self_color) or check_dia_right(x, y, self_color) or check_dia_left(x, y, self_color):
            return True
        
        return False
    
    # Logic
    for i, row in enumerate(table):
        for j, col in enumerate(row):
            cur_point = table[i][j]

            if cur_point:
                if does_win(i, j):
                    stone_in_the_middle = [i + 1, j + 3]

                    return {"color": cur_point, "coord": stone_in_the_middle}

    return 0

table = [list(map(int, input().split())) for _ in range(19)]
end_game = check_status(table)

if not end_game:
    print(end_game)
else:
    print(end_game["color"])
    for value in end_game["coord"]:
        print(value, end=" ")