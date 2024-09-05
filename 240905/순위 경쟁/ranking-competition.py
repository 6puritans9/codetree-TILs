n = int(input())
histories = []
for _ in range(n):
    student, score = input().split()
    
    histories.append((student, int(score)))

mapping = {"A":0, "B":1, "C":2}
scores = [0, 0, 0]
hof = [[0, 1, 2]]

for history in histories:
    student, change = history
    
    scores[mapping[student]] += change
    max_score = max(scores)

    new_hof = []
    for i, score in enumerate(scores):
        if score == max_score:
            new_hof.append(i)
    
    hof.append(new_hof)

count = 0
for i in range(1, len(hof)):
    cur = hof[i]
    prv = hof[i-1]

    if cur == prv:
        continue
    
    count += 1
    
print(count)