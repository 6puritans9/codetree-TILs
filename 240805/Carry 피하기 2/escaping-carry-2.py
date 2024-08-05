def is_carry(num1, num2):
    while num1 > 0 or num2 > 0:
        sub_num1 = num1 % 10
        sub_num2 = num2 % 10
        if sub_num1 + sub_num2 >= 10:
            return True
        num1 //= 10
        num2 //= 10
    return False

# Input reading
n = int(input())
numbers = [int(input()) for _ in range(n)]

answer = -1

# Iterate over all combinations of three different numbers
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if not is_carry(numbers[i], numbers[j]) and not is_carry(numbers[j], numbers[k]) and not is_carry(numbers[i], numbers[k]):
                candidate = numbers[i] + numbers[j] + numbers[k]
                if candidate > answer:
                    answer = candidate

print(answer)