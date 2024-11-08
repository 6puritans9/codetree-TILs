def in_range(x, y, n, m):
    return 0<= x < n and 0<= y < m


def get_sum_1(table, n, m):
    fig_1 = [(-1, 0), (0, 0), (0, 1)]
    fig_2 = [(0, 1), (0, 0), (1, 0)]
    fig_3 = [(1, 0), (0, 0), (0, -1)]
    fig_4 = [(0, -1), (0, 0), (-1, 0)]

    max_sum = 0
    for y in range(n):
        for x in range(m):
            fig_1_sum = 0
            fig_2_sum = 0
            fig_3_sum = 0
            fig_4_sum = 0

            for dy, dx in fig_1:
                nx, ny = x+ dx, y + dy
                if not in_range(nx, ny, n, m):
                    break
                
                fig_1_sum += table[ny][nx]
            
            for dy, dx in fig_2:
                nx, ny = x+ dx, y + dy
                if not in_range(nx, ny, n, m):
                    break
                
                fig_2_sum += table[ny][nx]

            for dy, dx in fig_3:
                nx, ny = x+ dx, y + dy
                if not in_range(nx, ny, n, m):
                    break
                
                fig_3_sum += table[ny][nx]

            for dy, dx in fig_4:
                nx, ny = x+ dx, y + dy
                if not in_range(nx, ny, n, m):
                    break
                
                fig_4_sum += table[ny][nx]

            max_sum = max(max_sum, fig_1_sum, fig_2_sum, fig_3_sum, fig_4_sum)

    return max_sum


def get_sum_2(table, n, m):
    fig_1 = [(0, -1), (0, 0), (0, 1)]
    fig_2 = [(-1, 0), (0, 0), (1, 0)]
    
    max_sum = 0
    for y in range(n):
        for x in range(m):
            fig_1_sum = 0
            fig_2_sum = 0

            for dy, dx in fig_1:
                nx = x + dx
                if not in_range(nx, y, n, m):
                    break
                
                fig_1_sum += table[y][nx]
            
            for dy, dx in fig_2:
                ny = y + dy
                if not in_range(x, ny, n, m):
                    break
                
                fig_2_sum += table[ny][x]
            
            max_sum = max(max_sum, fig_1_sum, fig_2_sum)

    return max_sum


n, m = map(int, input().split())
table = [[int(num) for num in input().split()] for _ in range(n)]

result = max(get_sum_1(table, n, m), get_sum_2(table, n, m))
print(result)