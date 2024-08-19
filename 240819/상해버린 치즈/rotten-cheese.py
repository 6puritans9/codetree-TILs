people_count, cheese_count, len_eat_records, len_sick_records = tuple(map(int, input().split()))

# person, cheese, eat_time
eat_records = [tuple(map(int, input().split())) for _ in range(len_eat_records)]
# person, sick_time
sick_records = [tuple(map(int, input().split())) for _ in range(len_sick_records)]

eat_records.sort()
sick_records.sort()

# Get the bad cheese
potential_bad_cheese = [0] * (cheese_count + 1)
sick_idx = 0
for person, cheese, time in eat_records:
    if person != sick_records[sick_idx][0] and sick_idx + 1 < len_sick_records:
        sick_idx += 1

    sick_person, sick_time = sick_records[sick_idx]

    if person == sick_person and time <= sick_time:
        potential_bad_cheese[cheese] += 1


potential_patients = set()
max_eaten_bad_cheese = max(potential_bad_cheese)
for bad_cheese, eat_count in enumerate(potential_bad_cheese):
    if eat_count != max_eaten_bad_cheese:
        continue

    for person, cheese, time in eat_records:
        if cheese == bad_cheese:
            potential_patients.add(person)

print(len(potential_patients))