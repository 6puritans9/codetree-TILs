N = int(input())
Hs = [int(input()) for _ in range(N)]

max_height = max(Hs) - 1
min_height = min(Hs)

max_icebergs = 0
for surface_height in range(max_height, min_height - 1, -1):
    new_Hs = [h - surface_height for h in Hs]
    count = 0

    for i in range(N):
        if new_Hs[i] > 0 and i == N - 1 or new_Hs[i] > 0 and new_Hs[i+1] <= 0:
            count += 1
        else:
            continue

    max_icebergs = max(max_icebergs, count)

print(max_icebergs)