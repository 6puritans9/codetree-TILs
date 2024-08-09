def get_gcd(num1, num2):
    small, big = min(num1, num2), max(num1, num2)
    if not big % small:
        return big
    
    for i in range(2, small + 1):
        if not big % i:
            return i

    return 0


def get_lcm(numbers, n):
    index = n -1
    cur_number = numbers[index]
    if index == 0:
        return cur_number

    lcm_so_far = get_lcm(numbers, n - 1)
    gcd = get_gcd(cur_number, lcm_so_far)
    if not gcd:
        return cur_number * lcm_so_far

    return gcd * min(cur_number, lcm_so_far)


n = int(input())
numbers = list(map(int, input().split()))

print(get_lcm(numbers, n))