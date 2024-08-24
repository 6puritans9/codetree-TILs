def min_max_pebble(n, k, pebbles):
    dp = [float('inf')] * n
    dp[0] = pebbles[0]  # Start at the first pebble
    
    for i in range(1, n):
        for j in range(max(0, i-k), i):
            dp[i] = min(dp[i], max(dp[j], pebbles[i]))
    
    return dp[n-1]

# Read input
n, k = map(int, input().split())
pebbles = list(map(int, input().split()))

# Calculate and print the result
result = min_max_pebble(n, k, pebbles)
print(result)