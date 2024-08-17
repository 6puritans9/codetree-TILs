def get_sum(num):
    str_num = str(num)
    total_sum = 0

    for char in str_num:
        total_sum += int(char)

    return total_sum


X, Y = map(int, input().split())

max_value = 0
for num in range(X, Y + 1):
    max_value = max(max_value, get_sum(num))

print(max_value)