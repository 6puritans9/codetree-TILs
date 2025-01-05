def backtrack(costs, n, frm, cur_cost, cnt, visited, min_cost):
    # Prune if the current cost exceeds the minimum cost found so far
    if cur_cost >= min_cost[0]:
        return

    # If all cities are visited, return to the start
    if cnt == n - 1:
        cur_cost += costs[frm][0]
        if costs[frm][0] > 0:  # Ensure there's a valid path back to the start
            min_cost[0] = min(min_cost[0], cur_cost)
        return

    # Explore all unvisited cities
    for to in range(1, n):
        if not visited[to] and costs[frm][to] > 0:  # Valid unvisited city
            visited[to] = True
            backtrack(costs, n, to, cur_cost + costs[frm][to], cnt + 1, visited, min_cost)
            visited[to] = False


def get_min_cost(costs, n):
    # Initialize visited array and minimum cost
    visited = [False] * n
    visited[0] = True  # Start from city 0
    min_cost = [float("inf")]

    # Start backtracking from city 0
    backtrack(costs, n, 0, 0, 0, visited, min_cost)

    return min_cost[0]


if __name__ == "__main__":
    n = int(input())
    costs = [[int(num) for num in input().split()] for _ in range(n)]
    print(get_min_cost(costs, n))
