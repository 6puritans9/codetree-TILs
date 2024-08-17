n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            line_array = [0] * 101

            for l in range(n):
                if l == i or l == j or l == k:
                    continue

                start, end = lines[l]

                for x in range(start, end + 1):
                    line_array[x] += 1

            is_valid = True
            for section in line_array:
                if section > 1:
                    is_valid = False
                    break
            
            if is_valid:
                count += 1
            
print(count)