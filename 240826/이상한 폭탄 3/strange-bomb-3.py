def in_range(pos):
    return 0<= pos < N


def is_bomb_in_range(bomb_pos, bomb_number, bombs):
    start = bomb_pos + 1
    end = bomb_pos + bomb_number

    for i in range(start, end):
        if not in_range(i):
            break

        cur_bomb = bombs[i]
        if cur_bomb == bomb_number:
            return True

    return False


N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

result = 0
for i, bomb in enumerate(bombs):
    if is_bomb_in_range(i, bomb, bombs):
        result += 1

print(result)