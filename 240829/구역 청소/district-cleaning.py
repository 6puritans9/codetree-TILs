def get_intersection(a,b,c,d):
    if b > c and c > a:
        return b-c
    elif d > a and c < a:
        return d-a
    

a, b = map(int, input().split())
c, d = map(int, input().split())

cleaning_area = (b-a) + (d-c) - get_intersection(a,b,c,d)
print(cleaning_area)