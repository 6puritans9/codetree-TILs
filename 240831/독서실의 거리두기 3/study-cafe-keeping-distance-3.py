N = int(input())
seats = [int(num) for num in input()]

counts = set()
count = 0
for i, seat in enumerate(seats):
    if not seat:
        count += 1
    else:
        counts.add(count)
        count = 0
    
counts = sorted(list(counts))
counts[-1] = counts[-1] // 2
counts.sort()

print(counts[-1])