# def digitize(number):
#     binary = []

    
#     return binary


# def find_max(binaries):
#     max_binary = 0
    
#     return max_binary

# if __name__ == "__main__":
#     n, m = tuple(map(int, input().split()))
#     integers = list(map(int, input().split()))
#     binaries = []

#     for integer in integers:
#         binaries.append(digitize(integer))
        
#     answer = find_max(binaries)
#     decimal = 0
#     for element in answer:
#         decimal += element * 2^i

#     print(decimal)

from itertools import combinations

if __name__ == "__main__":
    # Input reading
    n, m = map(int, input().split())
    integers = list(map(int, input().split()))
    
    # Generate all subsets of size m
    max_xor = 0
    for subset in combinations(integers, m):
        xor_value = 0
        for num in subset:
            xor_value ^= num  # XOR of all elements in the subset
        max_xor = max(max_xor, xor_value)
    
    print(max_xor)
