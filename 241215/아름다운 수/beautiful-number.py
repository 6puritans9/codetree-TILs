def is_valid(str_num):
    numbers = [int(char) for char in str_num]
    result = {}

    for number in numbers:
        if number not in result:
            result[number] = 0
        result[number] += 1

    for number, count in result.items():
        if number != 1 and number != count:
            return False

    return True


def find_numbers(str_num, count, n):
    if len(str_num) == n:
        if is_valid(str_num):
            count[0] += 1
        return

    for i in range(1, 5):
        find_numbers(str_num + str(i), count, n)


n = int(input())
string = ""
count = [0]
find_numbers(string, count, n)
print(count[0])