def get_intersection(a,b,c,d):
    if b > c and c > a:
        return b-c
    elif d > a and c < a:
        return d-a
    elif c > a and d < b:
        return d-c
    elif a> c and b < d:
        return b-a
    
    return 0
    

a, b = map(int, input().split())
c, d = map(int, input().split())

cleaning_area = (b-a) + (d-c) - get_intersection(a,b,c,d)
print(cleaning_area)