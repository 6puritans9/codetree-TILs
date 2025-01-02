def backtrack(numbers, n, idx, sub_group, min_diff):
    if len(sub_group) == n:
        sum_sub_group = sum(numbers[i] for i in sub_group)
        cur_diff = abs(sum_sub_group - (sum(numbers) - sum_sub_group))
        min_diff[0] = min(min_diff[0], cur_diff)
        return
    if idx >= n*2:
        return
    
    sub_group.append(idx)
    backtrack(numbers, n, idx + 1, sub_group, min_diff)
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
