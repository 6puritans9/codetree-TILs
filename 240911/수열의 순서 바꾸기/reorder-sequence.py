def minimum_rotations(N, numbers):
    # Find the index where the sorted sequence should start
    start_index = 0
    for i in range(1, N):
        if numbers[i] < numbers[i-1]:
            start_index = i
            break
    
    # If the array is already sorted, start_index will be 0
    return start_index

# Read input
N = int(input())
numbers = list(map(int, input().split()))

# Compute and print the result
result = minimum_rotations(N, numbers)
print(result)