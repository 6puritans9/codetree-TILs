n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]

# Step 1: Find the global min and max with all segments included
global_min_start = min(x1 for x1, x2 in segments)
global_max_end = max(x2 for x1, x2 in segments)

# Step 2: Track the second min start and second max end (excluding one segment)
best_length = float('inf')

for i in range(n):
    # Exclude the i-th segment
    excluded = segments[i]

    # Find min start and max end excluding the current segment
    min_start = min(x1 for j, (x1, x2) in enumerate(segments) if j != i)
    max_end = max(x2 for j, (x1, x2) in enumerate(segments) if j != i)

    # Calculate the length of the segment that covers the remaining segments
    current_length = max_end - min_start
    best_length = min(best_length, current_length)

# Step 3: Output the shortest possible length
print(best_length)