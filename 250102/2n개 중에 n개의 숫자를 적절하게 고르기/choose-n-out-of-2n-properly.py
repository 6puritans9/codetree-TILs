def backtrack(numbers, n, idx, sub_group, min_diff):
    if len(sub_group) == n:
        other_group = [number for number in numbers if number not in sub_group]
        # print(other_group)
        cur_diff = abs(sum(sub_group) - sum(other_group))
        # print(cur_diff)
        # print("--------")
        min_diff[0] = min(min_diff[0], cur_diff)
        return
    if idx >= n*2:
        return
    
    for i in range(idx, n*2):
        sub_group.append(numbers[i])
        backtrack(numbers, n, i + 1, sub_group, min_diff)
        sub_group.pop()
    
    backtrack(numbers, n , idx + 1, sub_group, min_diff)


def get_min_diff(numbers, n):
    min_diff = [float("inf")]

    backtrack(numbers, n, 0, [], min_diff)
    return min_diff[0]


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    print(get_min_diff(numbers, n))
