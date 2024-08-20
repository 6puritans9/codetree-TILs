N = int(input())
Hs = [int(input()) for _ in range(N)]

max_height = max(Hs) - 1
min_height = min(Hs)

max_icebergs = 0
for surface_height in range(max_height, min_height - 1, -1):
    count = 0

    if Hs[0] > surface_height:
        count += 1
    
    for i in range(1, N):
        if Hs[i] > surface_height and Hs[i-1] <= surface_height:
            count += 1

    max_icebergs = max(max_icebergs, count)

print(max_icebergs)