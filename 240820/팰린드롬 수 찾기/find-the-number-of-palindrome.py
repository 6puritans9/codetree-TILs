def is_palindrome(str_num, length):
    for i in range(length // 2):
        if str_num[i] != str_num[-i -1]:
            return False
    
    return True


X, Y = tuple(map(int, input().split()))

count = 0
for num in range(X, Y + 1):
    str_num = str(num)
    length = len(str_num)

    if is_palindrome(str_num, length):
        count += 1

print(count)