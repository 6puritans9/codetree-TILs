# def is_overlapped(target_pos, comp_start, comp_end):
#     if comp_start <= target_pos <= comp_end:
#         return True

#     return False


x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

if x2 < a1 or x1 > a2 and y2 < b1 or y1 > b2:
    print("nonoverlapping")
elif a2 < x1 or a1 > x2 and b2 < y1 or b1 > y2:
    print("nonoverlapping")
else:
    print("overlapping")