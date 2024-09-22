n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    min = i

    for j in range(i+1, n):
        if numbers[j] < numbers[min]:
            min = j
        
    numbers[min], numbers[i] = numbers[i], numbers[min]

for number in numbers:
    print(number, end=" ")