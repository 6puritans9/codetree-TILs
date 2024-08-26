def get_numbers(sums):
    for i in range(LENGTH):
        for j in range(i + 1, LENGTH):
            for k in range(j + 1, LENGTH):
                for l in range(k + 1, LENGTH):
                    a, b, c, d = sums[i], sums[j], sums[k], sums[l]

                    all_sums = {
                        a, b, c, d,
                        a+b, b+c, c+d, d+a, a+c, b+d,
                        a+b+c, a+b+d, a+c+d, b+c+d,
                        a+b+c+d
                    }
                    if all_sums == set(sums):
                        return [a, b, c, d]

    return None

LENGTH = 15

sums = list(map(int, input().split()))
sums.sort()

result = get_numbers(sums)
if result:
    a, b, c, d = result
    print(a, b, c, d, end=" ")
else:
    print(None)