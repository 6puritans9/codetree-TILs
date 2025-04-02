def find_min_cost(n:int, k:int, numbers:list[int]) -> int:
    # TC = O(N) + O(NK)
    # SC = O(N)
    
    min_num = float("inf")
    max_num = 0
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number

    diff = max_num - min_num
    cost = 0
    while diff > k:
        count_min_nums = 0
        count_max_nums = 0
        min_indicies = []
        max_indicies = []

        for i, number in enumerate(numbers):
            if number == min_num:
                count_min_nums += 1
                min_indicies.append(i)
            if number == max_num:
                count_max_nums += 1
                max_indicies.append(i)
        
        if count_min_nums <= count_max_nums:
            for i in min_indicies:
                numbers[i] += 1
                cost += 1
            min_num += 1
        else:
            for i in max_indicies:
                numbers[i] -= 1
                cost += 1
            max_num -= 1

        diff -= 1
    
    return cost


if __name__ =="__main__":
    # For given N numbers,
    # mutate each number
    # to make the largest difference betwenn numbers <= K
    # Defineing a cost as abs(a-b),
    # find the minimum cost

    # Constratins
    # 1. 1 <= N <= 10^2
    # 2. 1 <= K <= 10^4
    # 3. 1 <= number <= 10^4
    # Time 5000ms
    # Space 288MiB

    # Approach
    # 1. Find the min number and max number
    # 2. if count(min_number) <= count(max_number):
    #       min_number += 1
    #   else:
    #       max_number += 1
    # 3. cost += count(numbers)
    # 4. repeat until the difference becomes <= K
    # 5. This will take O(N * (K - difference)) == O(10^2 * 10^4) = 6/8 * 10^3 ms

    n, k = map(int, input().split())
    numbers = [int(num) for num in input().split()]

    print(find_min_cost(n, k, numbers))