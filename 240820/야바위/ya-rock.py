N = int(input())
steps = [tuple(int(num) for num in input().split()) for _ in range(N)]

max_point = 0
for starting_point in range(1, 4):
    stage = [False] * (N + 1)
    stage[starting_point] = True
    
    cur_point = 0
    for step in steps:
        a, b, c = step
        
        if stage[a]:
            stage[a], stage[b] = False, True
        elif stage[b]:
            stage[a], stage[b] = True, False
        
        if stage[c]:
            cur_point += 1
    
    max_point = max(max_point, cur_point)

print(max_point)