def init(N):
    people = []
    
    for _ in range(N):
        pos, char = input().split()
        pos = int(pos)
        people.append((pos, char))

    # Sort by position to ensure the correct order
    people.sort()
    
    return people

def find_max_distance(people):
    max_distance = 0
    num_people = len(people)
    
    for i in range(num_people):
        g_count = 0
        h_count = 0
        
        for j in range(i, num_people):
            if people[j][1] == 'G':
                g_count += 1
            else:
                h_count += 1
            
            if g_count == 0 or h_count == 0 or g_count == h_count:
                distance = people[j][0] - people[i][0]
                max_distance = max(max_distance, distance)
                
    return max_distance

N = int(input())
people = init(N)

max_distance = find_max_distance(people)
print(max_distance)