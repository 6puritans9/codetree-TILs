def init(N):
    people = []
    
    for _ in range(N):
        pos, char = input().split()
        pos = int(pos)
        people.append((pos, char))

    people.sort()
    
    return people


def find_max_distance(people, people_length):
    max_distance = 0
    
    for i in range(N):
        g_count = 0
        h_count = 0

        for j in range(i, N):
            if people[j][1] == "G":
                g_count += 1
            else:
                h_count += 1
        
            if g_count == 0 or h_count == 0 or g_count == h_count:
                max_distance = max(max_distance, people[j][0] - people[i][0])

    return max_distance


N = int(input())
people = init(N)

max_distance = find_max_distance(people, N)
print(max_distance)