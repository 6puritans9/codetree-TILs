def is_carry(num1, num2):
    sub_num1 = num1 % 10
    sub_num2 = num2 % 10
    if num1 < 10 or num2 < 10:
        return sub_num1 + sub_num2 >= 10

    if is_carry(num1 // 10, num2 // 10):
        return True
    
    return sub_num1 + sub_num2 >= 10
    
    

n = int(input())
numbers = [int(input()) for _ in range(n)]

answer = -1
for i in range(n-2):
    # print(i)
    for j in range(i+1, n-1):
        candidate = 0

        for k in range(j+1, n):
            if is_carry(numbers[j], numbers[k]):
                continue
            else:
                candidate = numbers[j] + numbers[k]
                # print(f"i:{numbers[i]}")
                # print(f"j:{numbers[j]}")
                # print(f"k:{numbers[k]}")
                # print(candidate)
    
        if is_carry(numbers[i], candidate):
            # print(f"i:{numbers[i]}")
            # print(f"candidate:{candidate}")
            continue
        else:
            new_answer = numbers[i] + candidate

            if new_answer > answer:
                answer = new_answer
            # print(f"candidate:{candidate}")
            # print(f"answer:{answer}")
        
        
print(answer)