import sys

def is_adjacent(seats, N):
    for i in range(1, N):
        if seats[i-1] and seats[i]:
            return True

    return False

N = int(input())
seats = [int(num) for num in input()]
if is_adjacent(seats, N):
    print(1)
    sys.exit(0)

counts = set()
count = 0
for i, seat in enumerate(seats):
    if not seat:
        count += 1
    else:
        if count:
            counts.add(count + 1)
        count = 0

counts = sorted(list(counts))
counts[-1] = counts[-1] // 2
counts.sort()

print(counts[0])