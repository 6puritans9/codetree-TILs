def find_pairs(n:int, cows:list[int]) -> int:
    pairs = 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if cows[i] <= cows[j] <= cows[k]:
                    pairs += 1

    return pairs


if __name__ == "__main__":
    n = int(input())
    cows = [int(num) for num in input().split()]

    print(find_pairs(n, cows))