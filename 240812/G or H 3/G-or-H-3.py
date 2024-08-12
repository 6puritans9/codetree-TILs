MAX_INDEX = 101

N, K = list(map(int, input().split()))
if K >= MAX_INDEX:
    K = MAX_INDEX - 1

peoples = [0] * MAX_INDEX

for _ in range(N):
    idx, char = input().split()
    idx = int(idx)

    peoples[idx] = 1 if char == "G" else 2
    
max_sum = 0    
for i in range(1, MAX_INDEX - K + 1):
    cur_sum = sum(peoples[i:i+K+1])

    max_sum = max(max_sum, cur_sum)

print(max_sum)