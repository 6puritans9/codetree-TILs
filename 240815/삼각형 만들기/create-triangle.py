def get_width(x1, x2, x3, y1, y2, y3):
    if not y1 == y2 == y3:
        if y1 == y2:
            return abs(x1 - x2)
        elif y2 == y3:
            return abs(x2 - x3)
        else:
            return abs(x3 - x1)
    
    return 0


def get_height(x1,x2, x3, y1,y2, y3):
    if not x1 == x2 == x3:
        if x1 == x2:
            return abs(y1 - y2)
        elif x2 == x3:
            return abs(y2 - y3)
        else:
            return abs(y3 - y1)
    
    return 0


N = int(input())
dots = [tuple(int(num) for num in input().split()) for _ in range(N)]

max_area = 0
for i in range(N):
    max_width = 0
    max_height = 0

    for j in range(i+1, N):
        for k in range(j+1, N):
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            x3, y3 = dots[k]

            width = get_width(x1, x2, x3, y1, y2, y3)
            height = get_height(x1, x2, x3, y1, y2, y3)

            max_width = max(max_width, width)
            max_height = max(max_height, height)

    max_area = max(max_area, max_width * max_height)

print(max_area)