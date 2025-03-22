def find_min_cost(n:int, h:int, t:int, fields:list[int]) -> int:
    min_cost = float("inf")

    for i in range(n - t):
        cur_cost = 0

        for j in range(i, i+t):
            cur_cost += abs(h - fields[j])

        min_cost = min(min_cost, cur_cost)

    return min_cost


if __name__ == "__main__":
    # N numbers of fields are given
    # Raising or lowering field costs 1
    # To make consecutive fields having height H at least T times,
    # find the minimum cost

    # Constraints
    # 1 <= N, H <= 100
    # 1 <= T <= min(N, 10)
    # 0 <= height <= 200

    # Approach
    # 1. for i in range(N - T):
    #       for j in range(i, i+T+1):
    #           if in_range(j, n):
    #               get current_cost
    # 2. This will take O(N^2)

    n, h, t = map(int, input().split())
    fields = [int(num) for num in input().split()]

    print(find_min_cost(n, h, t, fields))