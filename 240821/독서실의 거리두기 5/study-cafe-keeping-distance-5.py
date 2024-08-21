N = int(input())
seats = list(map(int, input()))

max_distance = 0
empty_seats = []
for i, seat in enumerate(seats):

    if not seat:
        empty_seats.append(0)
    elif seat and len(empty_seats):
        distance = (len(empty_seats) // 2) + 1
        max_distance = max(max_distance, distance)
        empty_seats.clear()

    if i == N-1 and len(empty_seats):
        distance = (len(empty_seats) // 2)
        max_distance = max(max_distance, distance) 

print(max_distance)