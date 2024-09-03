n = int(input())
numbers = list(map(int, input().split()))

# pos[number][0] = index
# pos[number][1] = counts
results = [[None, 0] for _ in range(101)]


ans = -1
for i, number in enumerate(numbers):
    if not results[number][0]:
        results[number][0] = i + 1
        results[number][1] += 1
    else:
        results[number][1] += 1

did_pass_first = False
for result in results:
    if not did_pass_first and result[0]:
        did_pass_first = True
    elif did_pass_first and result[0] and result[1] == 1:
        ans = result[0]
        break
    elif did_pass_first and reulst[0] and rsult[1] > 1:
        break

print(ans)