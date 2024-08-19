N, M, D, S = map(int, input().split())

# Store eating records: (person, cheese, time)
eating_records = [tuple(map(int, input().split())) for _ in range(D)]

# Store sick records: (person, time)
sick_records = [tuple(map(int, input().split())) for _ in range(S)]

max_sick_people = 0

# Check each cheese
potentially_sick = set()
for cheese in range(1, M + 1):
    is_valid_candidate = False

    # Find all people who ate this cheese
    for person, eaten_cheese, eat_time in eating_records:
        if eaten_cheese == cheese:
            potentially_sick.add(person)

    # Check if this cheese is consistent with sick records
    for sick_person, sick_time in sick_records:
        for person, eaten_cheese, eat_time in eating_records:
            if (person == sick_person and 
                eaten_cheese == cheese and 
                eat_time == sick_time - 1):
                is_valid_candidate = True
                break
        if is_valid_candidate:
            break

    # Update max_sick_people if this is a valid candidate
    if is_valid_candidate or not sick_records:
        max_sick_people = max(max_sick_people, len(potentially_sick))

print(max_sick_people)