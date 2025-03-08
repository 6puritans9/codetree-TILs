def find_max_nonadjacent_sum(n:int, numbers:list[int]) -> int:
    # TC = O(N)
    # SC = O(1)
        
    max_sum = -float("inf")
    max_num = numbers[0]

    for i in range(2, n):
        max_sum = max(max_sum, numbers[i] + max_num)
        max_num = max(max_num, numbers[i-1])
        
    return max_sum


if __name__ == "__main__":
    # It also can be solved with a single iteration.
    # With two variables for index i: 1. max_sum, 2. the largest non-adjacent number(max_num),
    # Update them for each iteration:
    # max_sum = max(max_sum, cur_num + max_num)
    # max_num = max(max_num, numbers[i-1])

    n = int(input())
    numbers = [int(num) for num in input().split()]

    print(find_max_nonadjacent_sum(n, numbers))

    