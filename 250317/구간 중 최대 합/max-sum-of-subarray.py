def find_max_seq_sum(n:int, k:int, numbers:list[int]) -> int:
    # TC = O(n^2)
    # TC = O(1)
        
    max_sum = 0
    
    for i in range(n-k+1):
        cur_sum = 0
        
        for j in range(i, i+k):
            cur_sum += numbers[j]
        
        max_sum = max(max_sum, cur_sum)
    
    return max_sum 


if __name__ =="__main__":
    # 1 <= k <= n <= 100
    # 1 <= number <= 100
    # typical O(n^2) brute force will make it

    n, k = map(int, input().split())
    numbers = [int(num) for num in input().split()]

    print(find_max_seq_sum(n, k, numbers))
