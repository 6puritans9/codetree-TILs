def in_range(i, N):
    return 0 <= i < N


N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

max_num = -1
for i, bomb_1 in enumerate(bombs):
    for j in range(i+1, i+K+1):
        if not in_range(j, N):
            break

        bomb_2 = bombs[j]

        if bomb_1 == bomb_2:
            max_num = max(max_num, bomb_1)

print(max_num)