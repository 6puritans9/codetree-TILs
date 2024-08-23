n, m = map(int, input().split())
ranges = [[int(num) for num in input().split()] for _ in range(m)]
        
frequency = [0] * (n + 1)
for _range in ranges:
    x, y = _range
    if x > y:
        x, y = y, x

    frequency[x] += 1
    frequency[y] += 1

max_i, second_i = max(frequency), 0
for i, value in enumerate(frequency, start = 1):
    if second_i < value < max_i:
        second_i = value

print(second_i)