def can_cover_with_three_lines(dots):
    # Extract unique x and y values from the dots
    x_values = list(set(dot[0] for dot in dots))  # Vertical lines (x = constant)
    y_values = list(set(dot[1] for dot in dots))  # Horizontal lines (y = constant)
    
    # We need to try all combinations where the total number of lines is 3
    # We can have (3,0), (2,1), and (1,2) configurations of vertical and horizontal lines.
    
    # Case 1: 3 vertical lines
    if len(x_values) >= 3:
        for i in range(len(x_values)):
            for j in range(i + 1, len(x_values)):
                for k in range(j + 1, len(x_values)):
                    line_comb = [x_values[i], x_values[j], x_values[k]]
                    if all(dot[0] in line_comb for dot in dots):
                        return 1

    # Case 2: 2 vertical lines and 1 horizontal line
    if len(x_values) >= 2 and len(y_values) >= 1:
        for i in range(len(x_values)):
            for j in range(i + 1, len(x_values)):
                for k in range(len(y_values)):
                    line_comb_x = [x_values[i], x_values[j]]
                    line_comb_y = [y_values[k]]
                    if all(dot[0] in line_comb_x or dot[1] in line_comb_y for dot in dots):
                        return 1

    # Case 3: 1 vertical line and 2 horizontal lines
    if len(x_values) >= 1 and len(y_values) >= 2:
        for i in range(len(x_values)):
            for j in range(len(y_values)):
                for k in range(j + 1, len(y_values)):
                    line_comb_x = [x_values[i]]
                    line_comb_y = [y_values[j], y_values[k]]
                    if all(dot[0] in line_comb_x or dot[1] in line_comb_y for dot in dots):
                        return 1

    # Case 4: 3 horizontal lines
    if len(y_values) >= 3:
        for i in range(len(y_values)):
            for j in range(i + 1, len(y_values)):
                for k in range(j + 1, len(y_values)):
                    line_comb = [y_values[i], y_values[j], y_values[k]]
                    if all(dot[1] in line_comb for dot in dots):
                        return 1

    return 0

# Input handling
N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

# Determine if 3 lines can cover all dots
result = can_cover_with_three_lines(dots)
print(result)