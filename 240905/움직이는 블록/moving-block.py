N = int(input())
blocks = [int(input()) for _ in range(N)]

total_blocks = sum(blocks)
avg_blocks = total_blocks // N

ans = 0
for i in range(N):
    ans += abs(avg_blocks - blocks[i])

print(ans // 2)