n = int(input())
numbers = list(map(int, input().split()))
is_sorted = False

for i in range(n):
    is_sorted = True
    for j in range(1, n):
        if numbers[j-1] > numbers[j]:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            is_sorted = False
        
    if is_sorted:
        break

for number in numbers:
    print(number, end=" ")