def find_answer(k:int, n:int, ranks:list[tuple[int]]) -> int:
    # TC = O(K * N^2)
    # SC = O(1)
    
    count = 0

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            
            rank_a, rank_b = -1, -1
            for rank in ranks:
                for i in range(n):
                    if rank[i] == a:
                        rank_a = i
                    elif rank[i] == b:
                        rank_b = i
                
                if rank_a > rank_b:
                    break
            else:
                count += 1

    return count


if __name__ == "__main__":
    # Given N people and K numbers of matches,
    # find the number of sets (a, b),
    # that rank(a) > rank(b) for K times

    # Constraints
    # 1 <= K <= 10
    # 1 <= N <= 20
    
    # Approach
    # 1. Make combinations O(N^2)
    # 2. For each line of ranks:  O(K)
    #       if not rank(a) > rank(b):
    #           break
    #       count += 1
    
    k, n = map(int, input().split())
    ranks = []
    for _ in range(k):
        ranks.append(tuple(int(num) for num in input().split()))

    print(find_answer(k, n, ranks))

