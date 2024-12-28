# def in_range(x, n):
#     return 0<= x < n


# # def backtrack(numbers, n, idx):
# #     if not in_range(idx, n) or numbers[idx] == 0:
# #         return -1


# def jump(numbers, n, idx, count):
#     global min_count

#     max_jump_dist = numbers[idx]
#     goal = n-1

#     if not in_range(idx, n) or max_jump_dist == 0:
#         min_count = -1
#         return

#     if idx == goal:
#         print("goal")
#         print(count)
#         if min_count == - 1:
#             min_count = count
#             return 

#         min_count = min(min_count, count)
#         return

#     for i in range(1, max_jump_dist + 1):
#         jump(numbers, n, idx + i, count + 1)
    

# if __name__ == "__main__":
#     n = int(input())
#     numbers = [int(num) for num in input().split()]
#     min_count = float("inf")

#     jump(numbers, n, 0, 0)
#     print(min_count)

def min_jumps(numbers, idx, n):
    # If already at the last position
    if idx == n - 1:
        return 0

    # If the current position is out of bounds or cannot jump further
    if idx >= n or numbers[idx] == 0:
        return float('inf')  # Represents an unreachable path

    # Explore all possible jumps from the current position
    min_steps = float('inf')
    max_jump = numbers[idx]

    for step in range(1, max_jump + 1):
        # Recursive call to check the number of jumps from the next position
        result = min_jumps(numbers, idx + step, n)
        min_steps = min(min_steps, result)

    # If min_steps is infinity, it means this path is unreachable
    return min_steps + 1 if min_steps != float('inf') else float('inf')

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    result = min_jumps(numbers, 0, n)
    print(result if result != float('inf') else -1)
