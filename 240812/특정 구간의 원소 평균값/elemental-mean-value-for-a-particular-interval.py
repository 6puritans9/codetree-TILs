N = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(i+1, N+1):
        avg = sum(numbers[i:j]) / (j - i)
        # print(f"i:{i}, j:{j}, sum:{sum(numbers[i:j])}, j-i:{j-i} avg:{avg}")
        
        if avg in numbers[i:j]:
            # print(f"{avg} is in")
            count +=1 

print(count)