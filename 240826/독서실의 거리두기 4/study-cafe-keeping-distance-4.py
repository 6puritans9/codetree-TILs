def get_min_dist(n, seats):
    dist = n

    for i in range(n):
        for j in range(i+1, n):
            if seats[i] == 1 and seats[j] == 1:
                dist = min(dist, j - i)
    
    return dist


N = int(input())
seats = [int(num) for num in input()]

result = 0
for i in range(N):
    if not seats[i]:
        seats[i] = 1
        
        for j in range(i+1, N):
            if not seats[j]:
                seats[j] = 1
                result = max(result, get_min_dist(N, seats))
                seats[j] = 0
        
        seats[i] = 0

print(result)