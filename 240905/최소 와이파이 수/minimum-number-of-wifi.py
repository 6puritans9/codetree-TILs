n, m = map(int, input().split())
bits = list(map(int, input().split()))
cost = 0

i = 0
while i < n:
    if bits[i]:
        cost += 1
        i += 2*m + 1
        continue
    
    i += 1

print(cost)