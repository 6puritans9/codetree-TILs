import sys

n = int(input())
seats = [int(num) for num in input()]

max_dist = 0
first_idx, last_idx = None, None
for i in range(n):
    if seats[i]:
        for j in range(i+1, n):
            if seats[j]:
                cur_dist = j - i

                if cur_dist > max_dist:
                    max_dist = cur_dist
                    first_idx, last_idx = i, j

                break

max_dist2 = 0
far_side_idx = None
if not seats[0]:
    dist = 0
    for i in range(0, n):
        if seats[i]:
            break
        dist += 1
    
    if dist > max_dist2:
        max_dist2 = dist
        far_side_idx = 0

if not seats[n-1]:
    dist = 0
    for i in range(n-1, -1, -1):
        if seats[i]:
            break
        dist += 1
    
    if dist > max_dist2:
        max_dist2 = dist
        far_side_idx = n-1

if max_dist2 >= max_dist // 2:
    seats[far_side_idx] = 1
else:
    seats[(first_idx + last_idx) // 2] = 1

min_max_dist = float("inf")
for i in range(n):
    if seats[i]:
        for j in range(i+1, n):
            if seats[j]:
                min_max_dist = min(min_max_dist, j-i)

                break

print(min_max_dist)