def get_valid_digits(d, N):
    return [((d - 1) + i) % N + 1 for i in range(-2, 3)]


def get_combinations(a,b,c,N):
    set_a = get_valid_digits(a, N)
    set_b = get_valid_digits(b, N)
    set_c = get_valid_digits(c, N)

    valid_combinations = set()

    for a in set_a:
        for b in set_b:
            for c in set_c:
                valid_combinations.add((a,b,c))

    return valid_combinations


N = int(input())
a1, b1, c1 = tuple(map(int, input().split()))
a2, b2, c2 = tuple(map(int, input().split()))

combination_1 = get_combinations(a1,b1,c1,N)
combination_2 = get_combinations(a2,b2,c2,N)

total_combination = combination_1.union(combination_2)

print(len(total_combination))