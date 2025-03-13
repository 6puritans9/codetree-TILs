def find_min_diff(s:int, n:int, numbers:list[int]) -> int:
    # TC = O(N^2)
    # SC = O(1)
    
    total_sum = sum(numbers)
    min_diff = float("inf")

    for i in range(n):
        for j in range(i+1, n):
            num1, num2 = numbers[i], numbers[j]

            exclude_sum = total_sum - (num1 + num2)
            diff = abs(s - exclude_sum)
            min_diff = min(min_diff, diff)
            
    return min_diff


if __name__ =="__main__":
    # With given N numbers, make combinations of NC(N-2)
    # Find one that makes to the closest given S, which exclude NC(N-2)
    # The possible maximum combination is 100N100,
    # which takes up to O(N^2) time to make 100 combinations
    # that can be done easily in 5000ms
    
    # Print the difference between S and the closest to S

    n, s = map(int, input().split())
    numbers = [int(num) for num in input().split()]

    print(find_min_diff(s, n, numbers))