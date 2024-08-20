A, B, C = tuple(map(int, input().split()))
result = 0

sum_As = [A * i for i in range((C // A) + 1)]
sum_Bs = [B * i for i in range((C // B) + 1)]

max_sum = 0
for sum_A in sum_As:
    for sum_B in sum_Bs:
        temp_sum = sum_A + sum_B

        if temp_sum > C:
            break

        max_sum = max(max_sum, temp_sum)

print(max_sum)