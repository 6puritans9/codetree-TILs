def max_min_difference_groups(n, numbers):
    # Sort the array in descending order
    numbers.sort()
    
    # Calculate the minimum difference between elements n positions apart
    min_diff = min(numbers[i+n] - numbers[i] for i in range(n))
    
    return min_diff

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Compute and print the result
result = max_min_difference_groups(n, numbers)
print(result)