n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

for number in numbers:
    print(number, end=" ")
print()

reversed_numbers = list(reversed(numbers))
for number in reversed_numbers:
    print(number, end=" ")