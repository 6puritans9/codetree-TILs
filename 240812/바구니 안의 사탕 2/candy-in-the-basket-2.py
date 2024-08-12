MAX_INDEX = 101

N, K = list(map(int, input().split()))
candies = [0] * MAX_INDEX

for _ in range(N):
    amount, pos = list(map(int, input().split()))
    pos = int(pos)

    candies[pos] += amount

max_sum = 0
for i in range(1, (MAX_INDEX - K + 1)):
    current_sum = sum(candies[i:i + (K * 2 + 1)])

    max_sum = max(max_sum, current_sum)

print(max_sum)