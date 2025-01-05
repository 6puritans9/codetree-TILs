def generate_permutations(visited, n, count, permutation):
    if count == n:
        print(" ".join(map(str, permutation)))
        return
    
    for i in range(n, 0, -1):
        if not visited[i]:
            permutation.append(i)
            visited[i] = True
            generate_permutations(visited, n, count + 1, permutation)
            permutation.pop()
            visited[i] = False


if __name__ == "__main__":
    n = int(input())
    visited = [False] * (n + 1)
    generate_permutations(visited, n, 0,[])
