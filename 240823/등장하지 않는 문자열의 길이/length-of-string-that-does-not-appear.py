def compare_string(_string, N):
    length = 1
    half_string_length = (N // 2) + 1

    answer = 0
    while length <= half_string_length:
        for j in range(N - length):
            target_string = _string[j:j + length]

            for k in range(j + 1, (j + 1)+length):
                cur_string = _string[j+1:j+1+length]

                if j + 1 + length > N - length or target_string == cur_string:
                    break
                
            answer = length
        
        length += 1

    return answer


N = int(input())
_string = [char for char in input()]

answer = compare_string(_string, N)
print(answer)