people, cheese, cheese_eaten, sick_people = tuple(map(int, input().split()))

# people_idx, cheese_idx, eat_time
cheese_info = [[int(num) for num in input().split()] for _ in range(cheese_eaten)]
# people_idx, sick_time
sick_info = [[int(num) for num in input().split()] for _ in range(sick_people)]

# how to solve
# 1. validate bad cheese
# 1-1. it can be narrowed down to less than sick people's eat_time(cheeses_eaten_idx)

# 2. find those who had eaten bad cheese
# 3. count the number of people(get rid of duplicates)
# 4. 

# Get the bad cheese
bad_cheese_candidates = [0] * (cheese + 1)
innocent_cheese = [1] * (cheese + 1)
for info_1 in sick_info:
    sick_people_idx, sick_time = info_1
    
    for info_2 in cheese_info:
        people_idx, cheese_idx, eat_time = info_2

        if people_idx == sick_people_idx and eat_time < sick_time:
            bad_cheese_candidates[cheese_idx] += 1
        else:
            innocent_cheese[cheese_idx] = 0

sick_people_candidates = set()
# Find who else had the bad cheese
for info in cheese_info:
    people_idx, cheese_idx, eat_time = info
    
    if bad_cheese_candidates[cheese_idx] > 0 and not innocent_cheese[cheese_idx]:
        sick_people_candidates.add(people_idx)
    
print(len(sick_people_candidates))