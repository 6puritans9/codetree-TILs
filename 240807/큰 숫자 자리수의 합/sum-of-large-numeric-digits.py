def get_multiplication(numbers):
    result = 1
    for number in numbers:
        result *= number
    
    return result
    

def recursive_sum(num):
    _sum = num % 10
    
    if num // 10 == 0:
        return num

    return _sum + recursive_sum(num // 10)
    

numbers = list(map(int, input().split()))
multiplication = get_multiplication(numbers)
print(recursive_sum(multiplication))