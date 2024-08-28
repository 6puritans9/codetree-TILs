def is_intersecting(point, range_start, range_end):
    if range_start <= point <= range_end:
        return True

    return False


x1, x2, x3, x4 = map(int, input().split())
if is_intersecting(x1, x3, x4) or is_intersecting(x2, x3, x4) or is_intersecting(x3, x1, x2) or is_intersecting(x4, x1, x2):
    print("intersecting")
else:
    print("nonintersecting")