def find_max_nonadjacent_sum(n:int, numbers:list[int]) -> int:
    # TC = O(N^2)
    # SC = O(1)

    max_sum = 0
    
    for i in range(2, n):
        for j in range(i-1):
            max_sum = max(max_sum, numbers[i] + numbers[j])

    return max_sum


if __name__ == "__main__":
    # In two nested loops, starting from i and j,
    # i iterates from 3 to n,
    # j iterates from 0 to n-2,
    # and find the maximum sum = numbers[i] + numbers[j]
    # This can be done in O(n^2), because the length of given input is n <= 100

    n = int(input())
    numbers = [int(num) for num in input().split()]

    print(find_max_nonadjacent_sum(n, numbers))

    