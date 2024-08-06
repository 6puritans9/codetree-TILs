def find_max(numbers, n):
    index = n-1
    if index == 0:
        return numbers[index]

    cur_number = numbers[index]

    return cur_number if cur_number > find_max(numbers, n -1) else find_max(numbers, n -1)
    


n = int(input())
numbers = list(map(int, input().split()))

print(find_max(numbers, n))