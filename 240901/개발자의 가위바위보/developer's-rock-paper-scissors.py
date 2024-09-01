N = int(input())
numbers = [tuple(int(num) for num in input().split()) for _ in range(N)]

wins = 0
for number in numbers:
    i, j = number
    if i == (j % 3) + 1:
        wins += 1

print(wins)