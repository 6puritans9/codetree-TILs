def radix_sort(numbers, n, max_num_digits):
    for i in range(1, max_num_digits + 1):
        digits = [[] for _ in range(10)]

        for j in range(n):
            number = numbers[j]
            digit = (number // pow(10, i - 1)) % 10

            digits[digit].append(number)

    result = []
    for digit_list in digits:
        result.extend(digit_list)

    numbers = result

    return numbers


n = int(input())
numbers = list(map(int, input().split()))
max_num_digits = len(str(max(numbers)))

new_numbers = radix_sort(numbers, n , max_num_digits)
for number in new_numbers:
    print(number, end = " ")