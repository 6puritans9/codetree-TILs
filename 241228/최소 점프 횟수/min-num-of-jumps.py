def in_range(x, n):
    return 0<= x < n


# def backtrack(numbers, n, idx):
#     if not in_range(idx, n) or numbers[idx] == 0:
#         return -1


def jump(numbers, n, idx, count):
    global min_count

    max_jump_dist = numbers[idx]
    goal = n-1

    if not in_range(idx, n) or max_jump_dist == 0:
        # print("out of range")
        min_count = -1
        return

    if idx == goal:
        print("goal")
        print(count)
        if min_count == - 1:
            min_count = count
            return 

        min_count = min(min_count, count)
        return

    for i in range(1, max_jump_dist + 1):
        # print("jump")
        jump(numbers, n, idx + i, count + 1)
    

if __name__ == "__main__":
    n = int(input())
    numbers = [int(num) for num in input().split()]
    min_count = float("inf")

    jump(numbers, n, 0, 0)
    print(min_count)
