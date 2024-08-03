user_string = input()


max_cnt = 0
for i in range(len(user_string)):
    if user_string[i] != "(":
        continue

    for j in range(i+1, len(user_string)):
        if user_string[j] == ")":
            max_cnt += 1
        
print(max_cnt)