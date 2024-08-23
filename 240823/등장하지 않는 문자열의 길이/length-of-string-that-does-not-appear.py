def min_unique_substring_length(N, _string):
    for length in range(1, N + 1):
        seen_substrings = set()
        for i in range(N - length + 1):
            substring = _string[i:i + length]
            if substring in seen_substrings:
                break
            seen_substrings.add(substring)
        else:
            return length

N = int(input())
_string = input()

answer = min_unique_substring_length(N, _string)
print(answer)