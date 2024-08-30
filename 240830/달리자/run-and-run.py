n = int(input())
As = [int(num) for num in input().split()]
Bs = [int(num) for num in input().split()]

total_move = 0
for i in range(n-1, -1, -1):
    cur_move = abs(Bs[i] - As[i])
    As[i - 1] -= cur_move
    total_move += cur_move

print(total_move)