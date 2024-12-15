def get_numbers(k, n, string=""):
    if len(string) == n:
        yield string
        return

    for i in range(1, k + 1):
        yield from get_numbers(k, n, string + str(i))


k, n = tuple(map(int, input().split()))

for result in get_numbers(k, n):
    print(" ".join(result))
