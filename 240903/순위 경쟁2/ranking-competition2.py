import math

n = int(input())
score_a = 0
score_b = 0
best_score = -math.inf
histories = [None]

for _ in range(n):
    student, score = input().split()
    score = int(score)

    if student == "A":
        score_a += score
    else:
        score_b += score

    if score_a >= best_score and score_b >= best_score and score_a == score_b:
        histories.append(("A", "B"))
    elif score_a >= best_score and score_a >= score_b:
        histories.append(("A"))
    elif score_b >= best_score and score_b >= score_a:
        histories.append(("B"))
    best_score = max(best_score, score_a, score_b)

count = 0
for i in range(1, len(histories)):
    cur_history = histories[i]
    prv_history = histories[i-1]

    if cur_history != prv_history:
        count += 1

print(count)