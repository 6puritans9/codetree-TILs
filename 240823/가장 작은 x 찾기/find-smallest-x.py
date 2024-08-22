def in_range(num, ranges):
    for i, _range in enumerate(ranges):
        start, end = _range
        
        if not start <= num * (2 ** (i + 1)) <= end:
            return False
        
    return True


n = int(input())
ranges = [[int(num) for num in input().split()] for _ in range(n)]

i = 1
while i:
    if in_range(i, ranges):
        print(i)
        break
    
    i += 1