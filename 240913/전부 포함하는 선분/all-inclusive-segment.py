n = int(input())
lines = [[int(num) for num in input().split()] for _ in range(n)]

min_start = float("inf")
max_end = 0
for x1, x2 in lines:
    if x1 < min_start:
        min_start = x1
    
    if x2 > max_end:
        max_end = x2

len_1 = 0
len_1_start = float("inf")
for x1, x2 in lines:
    if x1 == min_start:
        continue
    
    elif x1 < len_1_start:
        len_1_start = x1

len_1 = max_end - len_1_start

len_2 = 0
len_2_end = 0
for x1, x2 in lines:
    if x2 == max_end:
        continue
    
    elif x2 > len_2_end:
        len_2_end = x2

len_2 = len_2_end - min_start

print(min(len_1, len_2))