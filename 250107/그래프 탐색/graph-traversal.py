def dfs(node, graph, visited):
    visited[node] = True
    count = 1

    for neighbour in range(1, n + 1):
        if graph[node][neighbour] and not visited[neighbour]:
            count += dfs(neighbour, graph, visited)

    return count


def count_connections(edges, graph, n, m):
    visited = [False] * (n + 1)

    return dfs(1, graph, visited) - 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for a, b in edges:
        graph[a][b] = 1
        graph[b][a] = 1

    print(count_connections(edges, graph, n, m))
