def find_max_candies(n:int, k:int, baskets:list[int, int]) -> int:
    # TC = O(NlogN) + O(N) = O(NlogN)
    # SC = O(1)
    
    max_candies = 0
    cur_candies = 0
    
    left = 0
    for right in range(n):
        pos, right_candies = baskets[right]
        cur_candies += right_candies

        while pos - baskets[left][0] > k * 2:
            left_candies = baskets[left][1]
            cur_candies -= left_candies
            left += 1
        
        max_candies = max(max_candies, cur_candies)

    return max_candies


if __name__ == "__main__":
    # On a single line are N baskets which contains candies
    # Set a position c, find a subarray [c-K, c+K] that can hold the most candies

    # Constraints:
    # 1 <= N <= 100
    # 1 <= K <= 200
    # 0 <= position of each basket <= 100 (baskets can overlap)
    # 1 <= number of candies in a basket <= 100

    # Approach:
    # As baskets <= 100, length <= 100, brute force TC could go up to O(N^2) == O(10^4)
    # Can it go down to O(N) with sliding window?
    # 1. sort the baskets according to the pos
    # 2. set a return value max_candies
    # 3. for c in range(k, n-k), add candies and compare to the max_candies
    # return max_candies

    n, k = map(int, input().split())
    baskets = []
    for _ in range(n):
        candies, pos = map(int, input().split())
        baskets.append((pos, candies))

    baskets.sort(key=lambda x:x[0])
    
    print(find_max_candies(n, k, baskets))