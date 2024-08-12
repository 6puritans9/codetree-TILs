def is_matching(target_seq, target_seq_length, sub_seq):
    checked = [0] * target_seq_length
    
    for num1 in sub_seq:
        for j, num2 in enumerate(target_seq):
            if num1 == num2 and not checked[j]:
                checked[j] = 1

    if sum(checked) == target_seq_length:
        return True

    return False

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0

for i in range(N - M + 1):
    sub_seq = A[i:i+M]

    if is_matching(B, M, sub_seq):
        count += 1
        
print(count)