def radix_sort(numbers, max_num_digits):
    for i in range(1, max_num_digits + 1):
        digits = [[] for _ in range(10)]

        for number in numbers:
            digit = (number // pow(10, i - 1)) % 10
            digits[digit].append(number)

        numbers = [num for sublist in digits for num in sublist]

    return numbers


n = int(input())
numbers = list(map(int, input().split()))
max_num_digits = len(str(max(numbers)))

new_numbers = radix_sort(numbers, max_num_digits)
for number in new_numbers:
    print(number, end=" ")