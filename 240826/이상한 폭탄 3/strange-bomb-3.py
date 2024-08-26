def in_range(pos):
    return 0<= pos < N


def is_bomb_in_range(bomb_pos, bomb_number, bombs):
    start = bomb_pos + 1
    end = bomb_pos + K

    for i in range(start, end + 1):
        if not in_range(i):
            break

        cur_bomb = bombs[i]
        if cur_bomb == bomb_number:
            return True

    return False


MAX_NUMBER = 1000000

N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

result = 0
bombs_to_explode = [0] * (MAX_NUMBER + 1)
for i, bomb in enumerate(bombs):

    if is_bomb_in_range(i, bomb, bombs):
        bombs_to_explode[bomb] += 1

    
for i in range(MAX_NUMBER + 1):
    if bombs_to_explode[i] > result:
        result = i

print(result)