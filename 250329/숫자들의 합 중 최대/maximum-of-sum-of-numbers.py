def find_max_digit_sum(x:int, y:int) -> int:
    # TC = O(y-x+1)
    # SC = O(1)
    
    max_digit_sum = 0

    for n in range(x, y+1):
        number = n
        digit_sum = 0
        
        while number:
            digit_sum += number % 10
            number //= 10
        
        max_digit_sum = max(max_digit_sum, digit_sum)

    return max_digit_sum


if __name__ == "__main__":
    # For given X, Y,
    # find a number 
    # 1. in which ranges (X, Y+1),
    # 2. the sum of each digit is the largest

    # Constraints
    # 1 <= X <= Y <= 10^4
    # Time 5000ms
    # Space 288MiB

    # Approach
    # 1. The maxmimum length of digits is 4.
    # 2. The time complexity for brute force will be O(4 * 10^4) == 500ms
    
    x, y = map(int, input().split())
    print(find_max_digit_sum(x, y))