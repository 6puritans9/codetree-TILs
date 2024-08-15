def is_crossed(left_dot, right_dot):
    start_left_dot = left_dot[0]
    end_left_dot = left_dot[1]

    start_right_dot = right_dot[0]
    end_right_dot = right_dot[1]

    if start_right_dot < end_left_dot and end_right_dot <= end_left_dot:
        return True
    
    return False


N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]
dots.sort()

crossing_set = set()
for i in range(N):
    for j in range(i+1, N):
        if not is_crossed(dots[i], dots[j]):
            continue
        
        crossing_set.add(dots[i])
        crossing_set.add(dots[j])

print(len(crossing_set))