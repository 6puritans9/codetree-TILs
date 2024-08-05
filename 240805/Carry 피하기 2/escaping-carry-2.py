def no_carry(a, b, c):
    while a > 0 or b > 0 or c > 0:
        digit_sum = (a % 10) + (b % 10) + (c % 10)
        if digit_sum >= 10:
            return False
        a //= 10
        b //= 10
        c //= 10
    return True

n = int(input())
numbers = [int(input()) for _ in range(n)]
answer = -1

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if no_carry(numbers[i], numbers[j], numbers[k]):
                current_sum = numbers[i] + numbers[j] + numbers[k]
                answer = max(answer, current_sum)

print(answer)