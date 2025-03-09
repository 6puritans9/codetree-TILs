def has_carry(num1, num2, num3) -> bool:
    
    rem1, rem2, rem3 = num1 % 10, num2 % 10, num3 % 10
    while rem1 or rem2 or rem3:
        if rem1 + rem2 > 9 or rem2 + rem3 > 9 or rem3 + rem1 > 9:
            return True
        if rem1 + rem2 + rem3 > 9:
            return True
        
        num1 //= 10
        num2 //= 10
        num3 //= 10
        rem1, rem2, rem3 = num1 % 10, num2 % 10, num3 % 10

    return False


def find_max_sum_wo_carry(n:int, numbers:list[int]) -> int:
    max_sum = -1

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if has_carry(numbers[i], numbers[j], numbers[k]):
                    continue

                max_sum = max(max_sum, numbers[i] + numbers[j] + numbers[k])

    return max_sum


if __name__ =="__main__":
    # for each combination of three numbers,
    # check if adding each three digit will make carry(>= 10)
    # if not, update max_sum

    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    print(find_max_sum_wo_carry(n, numbers))
