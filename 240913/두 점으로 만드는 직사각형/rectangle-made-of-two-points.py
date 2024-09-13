x1, y1, x2, y2 = list(map(int, input().split()))
a1, b1, a2, b2 = list(map(int, input().split()))

ans_x1 = min(x1, a1)
ans_x2 = max(x2, a2)
ans_y1 = min(y1, b1)
ans_y2 = max(y2, b2)

len_x = ans_x2 - ans_x1
len_y = ans_y2 - ans_y1
print(len_x * len_y)