def get_result(num, count):
    if num <= 1:
        return count
    
    if num % 2:
        return get_result((num * 3) + 1, count + 1)
    else:
        return get_result(num // 2, count + 1)


n = int(input())
count = 0

print(get_result(n, count))