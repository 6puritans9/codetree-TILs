def get_gcd(num1, num2):
    small, big = min(num1, num2), max(num1, num2)
    
    while small:
        remainder = big % small
        big, small = small, remainder

    return big
        
        

def get_lcm(numbers, n):
    index = n -1
    cur_number = numbers[index]
    if index == 0:
        return cur_number

    lcm_so_far = get_lcm(numbers, n - 1)
    lcm = (lcm_so_far * cur_number) // get_gcd(lcm_so_far, cur_number)

    return lcm


n = int(input())
numbers = list(map(int, input().split()))

print(get_lcm(numbers, n))