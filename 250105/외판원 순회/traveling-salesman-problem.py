def backtrack(costs, n, frm, to, min_cost, cur_cost, cnt):
    global visited

    if cur_cost >= min_cost[0]:
        return
    if cnt == n - 1:
        cur_cost += costs[frm][0]
        min_cost[0] = min(min_cost[0], cur_cost)
        return
    if visited[to]:
        return

    if costs[frm][to]:
        visited[to] = True
        cost = cur_cost + costs[frm][to]
        for i in range(1, n):
            backtrack(costs, n, to, i, min_cost, cost, cnt + 1)
        visited[to] = False


def get_min_cost(costs, n):
    global visited

    min_cost = [float("inf")]

    for i in range(1, n):
        # visited[i] = True
        backtrack(costs, n, 0, i, min_cost, 0, 0)
        # visited[i] = False

    return min_cost[0]


if __name__ == "__main__":
    n = int(input())
    costs = [[int(num) for num in input().split()] for _ in range(n)]
    visited = [False] * n
    visited[0] = True

    print(get_min_cost(costs, n))
