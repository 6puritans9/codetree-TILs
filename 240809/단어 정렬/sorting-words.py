n = int(input())
strings = [input() for _ in range(n)]

strings.sort()

for string in strings:
    print(string)