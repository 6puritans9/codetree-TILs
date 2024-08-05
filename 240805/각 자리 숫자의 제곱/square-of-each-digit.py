def get_recursive_sum(n):
    if n < 10:
        return pow(n, 2)

    return get_recursive_sum(n // 10) + pow(n % 10, 2)


N = int(input())
print(get_recursive_sum(N))