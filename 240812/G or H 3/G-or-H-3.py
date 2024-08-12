def take_photo(peoples, peoples_size, photo_size):
    max_score = 0

    for i in range(1, peoples_size - photo_size + 1):
        interval_score = sum(peoples[i:i+photo_size + 1])
        max_score = max(max_score, interval_score)
    
    return max_score


N, K = list(map(int, input().split()))
peoples = [0] * 101
last_person_index = 0
score = {
    "G" : 1,
    "H": 2
}

for _ in range(N):
    idx, char = input().split()
    peoples[int(idx)] = score[char]
    last_person_index = max(int(idx), last_person_index)

print(take_photo(peoples, last_person_index, K))