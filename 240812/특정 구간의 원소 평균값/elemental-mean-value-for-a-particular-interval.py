N = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(i, N):
        avg = sum(numbers[j:N]) / (N - j)
        
        if avg in numbers[j:N]:
            count +=1 

print(count)