def find_min_time(x:int) -> int:
    left_dist = x
    cur_speed = 1
    time = 0

    while left_dist:
        time += 1
        left_dist -= cur_speed
        
        if left_dist >= (cur_speed+1)*(cur_speed+2)/2:
            cur_speed += 1
        elif left_dist >= cur_speed*(cur_speed+1)/2:
            continue
        else:
            cur_speed -= 1
        
    return time
        

if __name__ == "__main__":
    # 1. Going to run for X length
    # 2. Start from 1m/s, for every 1 sec, a decision should be made
    #   +1m/s or -1m/s or +0m/s
    # 3. The speed has to be 1m/s at the destination
    # 4. Speed cannot be 0m/s
    # 5. Find the minimum time to reach the destination
    
    # Constratins
    # Time 5000ms
    # Space 288MiB
    # 1 <= X <= 10^4
    
    # Approach
    # 1. Backtracking is not feasible due to its tc O(2^x)
    # 2. Set a state (cur_dist, cur_speed) for each step
    #       The final state should be (x, 1)
    # 3. From each state, I can make transition to:
    #       (cur_dist + 1, cur_speed + 1)
    #       (cur_dist + 1, cur_speed - 1)
    #       if cur_speed <=0: 
    #           return
    # 4. Use visited to avoid cycles
    # 5. BFS

    x = int(input())
    print(find_min_time(x))