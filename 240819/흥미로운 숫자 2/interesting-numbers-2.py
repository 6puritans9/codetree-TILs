def is_interesting(num):
    str_num = str(num)
    counts = [0] * 10

    for char in str_num:
        counts[int(char)] += 1

    count_1 = 0
    count_other = []
    for count in counts:
        if count == 1:
            count_1 += 1
        elif count != 0 and count != 1:
            count_other.append(count)

    if count_1 == 1 and len(count_other) == 1:
        return True

    return False


X, Y = map(int, input().split())

count = 0
for i in range(X, Y + 1):
    if is_interesting(i):
        count += 1

print(count)