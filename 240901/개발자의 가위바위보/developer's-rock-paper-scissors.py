def did_a_win(a, b):
    if a == "r" and b == "s" or a == "s" and b == "p" or a == "p" and b == "r":
        return True

    return False


N = int(input())
numbers = [tuple(int(num) for num in input().split()) for _ in range(N)]
mappings = [("r", "p", "s"), ("r", "s", "p"), ("s", "r", "p"), ("s", "p", "r"), ("p", "r", "s"), ("p", "s", "r")]

max_wins = 0
for mapping in mappings:
    cur_wins = 0

    for a, b in numbers:
        if a == b:
            continue

        map_a = mapping[a - 1]
        map_b = mapping[b - 1]

        if did_a_win(map_a, map_b):
            cur_wins += 1

    max_wins = max(max_wins, cur_wins)

print(max_wins)