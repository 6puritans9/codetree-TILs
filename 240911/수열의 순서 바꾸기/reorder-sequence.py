N = int(input())
numbers = list(map(int, input().split()))

biggest_num = 0
idx = 0
for i in range(N):
    cur_num = numbers[i]

    if cur_num > biggest_num:
        biggest_num = cur_num
        idx = i
        
print(idx+1)