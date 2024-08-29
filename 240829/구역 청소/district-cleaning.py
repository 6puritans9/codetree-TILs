def is_intersect(a,b,c,d):
    if b < c or d < a:
        return False

    return True


a, b = map(int, input().split())
c, d = map(int, input().split())

cleaning_area = 0
if is_intersect(a,b,c,d):
    cleaning_area = max(b,d) - min(a,c)
else:
    cleaning_area = (b-a) + (d-c)

print(cleaning_area)