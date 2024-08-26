N = int(input())
sums = list(map(int, input().split()))

sequence = [0] * N
for num in range(1, N + 1):
    is_valid = False
    used = []
    sequence[0] = num
    used.append(num)

    for idx in range(1, N):
        diff = sums[idx - 1] - sequence[idx - 1]
        sequence[idx] = diff

        if diff in used:
            break
        used.append(diff)

        if len(used) == N:
            is_valid = True
    
    if is_valid:
        break   
    
    
for num in sequence:
    print(num, end=" ")