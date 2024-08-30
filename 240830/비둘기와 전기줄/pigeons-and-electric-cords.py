N = int(input())

pigeons = [-1] * (11)
states = [[int(num) for num in input().split()] for _ in range(N)]

total_move = 0
for state in states:
    pigeon, pos = state

    if pigeons[pigeon] == -1:
        pigeons[pigeon] = pos
    elif pigeons[pigeon] != pos:
        pigeons[pigeon] = pos
        total_move += 1
    
print(total_move)