def get_intersection(a,b,c,d):
    if c < b and a < c and d>b:
        return b-c
    elif a < d and c < a and b>d:
        return d-a
    elif a < c and d < b:
        return d-c
    elif c < a and b < d:
        return b-a
    
    return 0
    

a, b = map(int, input().split())
c, d = map(int, input().split())

cleaning_area = (b-a) + (d-c) - get_intersection(a,b,c,d)
print(cleaning_area)