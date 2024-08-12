N, K = list(map(int, input().split()))
candies = [0] * 101

for _ in range(N):
    amount, pos = list(map(int, input().split()))
    pos = int(pos)

    candies[pos] += amount

max_sum = 0
for i in range(1, 102 - K * 2):
    current_sum = sum(candies[i:i+(K*2 + 1)])

    max_sum = max(max_sum, current_sum)

print(max_sum)