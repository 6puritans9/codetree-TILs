def get_sum(n):
    if n <= 2:
        return n 

    return n + get_sum(n - 2)


N = int(input())
print(get_sum(N))