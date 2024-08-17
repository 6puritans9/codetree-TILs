def get_work(temp, machine, C, G, H):
    min_temp, max_temp = machine
    
    if temp < min_temp:
        return C
    elif min_temp <= temp <= max_temp:
        return G
    else:
        return H


N, C, G, H = map(int, input().split())
machines = [tuple(map(int, input().split())) for _ in range(N)]

start, end = 1001, -1
for machine in machines:
    start = min(start, machine[0])
    end = max(end, machine[1])

max_total_work = 0
for temp in range(start, end + 1):
    total_work = 0
    
    for machine in machines:
        total_work += get_work(temp, machine, C, G, H)
    
    max_total_work = max(max_total_work, total_work)

print(max_total_work)