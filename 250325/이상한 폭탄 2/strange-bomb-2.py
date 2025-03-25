def in_valid_range(x:int, n:int) -> bool:
    return 0<= x < n


def find_largest_bomb(n:int, k:int, bombs:list[int]) -> int:
    # TC = O(N^2)
    # SC = O(1)
    
    max_bomb = 0
    
    for i in range(n):
        for j in range(i-k, i+k+1):
            if in_valid_range(j, n) and i != j and bombs[i] == bombs[j]:
                max_bomb = max(max_bomb, bombs[i])
                break

    return max_bomb if max_bomb else -1


if __name__ == "__main__":
    # For given N bombs, each bomb has numbers.
    # if bombs with same number are in K distance, they will explode.
    # Find the largest number that will explode.
    #    if none, return -1

    # Constraints
    # 1. 0 <= number <= 10^3
    # 2. 1 <= N <= 10^2
    # 3. 1 <= K <= N

    # Approach
    # 1. Simple exhaustive search with nested iteration O(N^2).
    # 2. For i in range(n):
    #       for j in range(i-k, i+k+1):
    #           if in_valid_range(j, n) and bombs[i] == bombs[j]:
    #               max_bomb = max(max_bomb, bombs[i])
    # 3. return max_bomb if max_bomb else -1
    
    n, k = map(int, input().split())
    bombs = [int(input()) for _ in range(n)]
    print(find_largest_bomb(n, k, bombs))