n, t = map(int, input().split())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))
lower.reverse()

for _ in range(t):
    upper_temp = upper[-1]
    lower_temp = lower[0]

    for i in range(n-1, 0, -1):
        upper[i] = upper[i-1]
    
    for j in range(n-1):
        lower[j] = lower[j+1]

    lower[-1] = upper_temp
    upper[0] = lower_temp

for num in upper:
    print(num, end=" ")
print()
for num in reversed(lower):
    print(num, end=" ")

