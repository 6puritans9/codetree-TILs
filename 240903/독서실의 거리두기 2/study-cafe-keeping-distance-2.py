import sys
import math


def is_adjacent(i, seats):
    if seats[i - 1] and seats[i]:
        return True

    return False


def get_min_dist(i, seats, n):
    dist = math.inf

    for i in range(n):
        for j in range(i + 1, n):
            if seats[i] and seats[j]:
                dist = min(dist, j - i)

    return dist


N = int(input())
seats = [int(num) for num in input()]
max_min_dist = 0

for i in range(N):
    if is_adjacent(i, seats):
        print(1)
        sys.exit(0)

    if i == 0 and not seats[i] and not seats[i+1] or i == N-1 and not seats[N-1] and not seats[N-2]:
        seats[i] = 1
        max_min_dist = max(max_min_dist, get_min_dist(i, seats, N))
        seats[i] = 0

    elif not seats[i] and not seats[i-1] and not seats[i+1]:
        seats[i] = 1
        max_min_dist = max(max_min_dist, get_min_dist(i, seats, N))
        seats[i] = 0

print(max_min_dist)