n, m, p = map(int, input().split())
messages = []
for _ in range(m):
    c, u = input().split()
    u = int(u)

    messages.append((c, u))

seen_users = set()
for i in range(p - 1, m):
    seen_users.add(messages[i][0])

all_users = []
for i in range(n):
    all_users.append(chr((ord("A") + i)))

results = []
for user in all_users:
    if user not in seen_users:
        results.append(user)

if p == 1 and not messages[p][1]:
    print("")
else:
    for result in results:
        print(result, end=" ")