def find_matching_cases(n:int, numbers:list[int]) -> int:
    # TC = O(N^2)
    # SC = O(1)
    result = 0

    for end in range(n):
        count = 0
        for start in range(end + 1):
            _sum = 0
            for i in range(start, end + 1):
                _sum += numbers[i]
            avg = _sum / (end-start+1)

            for i in range(start, end+1):
                if avg == numbers[i]:
                    count += 1
                    break

        result += count

    return result

# def find_matching_cases(n:int, numbers:list[int]) -> int:
#     # TC = O(N^2)
#     # SC = O(1)
#     result = 0

#     for end in range(n):
#         count = 0
#         for start in range(end + 1):
#             avg = sum(numbers[start:end+1]) / (end-start+1)

#             if avg in numbers[start:end+1]:
#                 count += 1
        
#         result += count

#     return result


if __name__ == "__main__":
    # In given N numbers,
    # from each subset, 
    # find if the average of the subset matches one of its element
    # return the number of possibilites
    
    # 1<=N<=100, 1<=number<=1000
    # Set the range of each subset O(N^2),
    # iterates once to find average O(N)
    # iterates twice to find matching element O(N)
    # O(N^2) + O(2N) = O(100^2)

    n = int(input())
    numbers = [int(num) for num in input().split()]

    print(find_matching_cases(n, numbers))
