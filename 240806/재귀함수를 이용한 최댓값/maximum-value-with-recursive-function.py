def find_max(numbers, n):
    index = n-1

    if index == 0:
        return numbers[index]

    cur_number = numbers[index]
    nxt_number = find_max(numbers, n-1)

    return cur_number if cur_number > nxt_number else nxt_number
    


n = int(input())
numbers = list(map(int, input().split()))

print(find_max(numbers, n))