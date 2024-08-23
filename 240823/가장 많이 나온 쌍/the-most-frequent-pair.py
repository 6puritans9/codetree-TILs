n, m = map(int, input().split())
ranges = [[int(num) for num in input().split()] for _ in range(m)]

max_result = 0        
for i, _range in enumerate(ranges):
    a, b = _range
    if a > b:
        a, b = b, a
    
    result = 0
    for j, _range2 in enumerate(ranges):
        x, y = _range2
        if x > y:
            x, y = y, x
        
        if a==x and b ==y:
            result += 1
        
    max_result = max(max_result, result)

print(max_result)