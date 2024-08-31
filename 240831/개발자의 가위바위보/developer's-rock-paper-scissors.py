N = int(input())
pairs = [[int(num) for num in input().split()] for _ in range(N)]

wins = 0
for pair in pairs:
    a, b = pair
    if a == b-1 or a == b+1:
        wins += 1

print(wins)