N, M, D, S = map(int, input().split())

cheese_info = []
sick_info = []

for _ in range(D):
    p, m, t = map(int, input().split())
    cheese_info.append((p, m, t))

for _ in range(S):
    p, t = map(int, input().split())
    sick_info.append((p, t))

potential_bad_cheeses = set()

for sick_person, sick_time in sick_info:
    for person, cheese, eat_time in cheese_info:
        if person == sick_person and eat_time < sick_time:
            potential_bad_cheeses.add(cheese)

max_sick_people = 0

for bad_cheese in potential_bad_cheeses:
    sick_candidates = set()
    for person, cheese, eat_time in cheese_info:
        if cheese == bad_cheese:
            sick_candidates.add(person)
    max_sick_people = max(max_sick_people, len(sick_candidates))

print(max_sick_people)