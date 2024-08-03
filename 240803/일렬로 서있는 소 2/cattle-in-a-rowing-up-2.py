def is_ascending(i,j,k):
    return i <= j <= k

N = int(input())
cows = list(map(int, input().split()))
length = len(cows)

count = 0
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            if is_ascending(cows[i], cows[j], cows[k]):
                count += 1

print(count)