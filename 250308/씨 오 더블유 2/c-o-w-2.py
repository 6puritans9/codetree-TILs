def find_possible_count(n: int, string:list[str]) -> int:
    # Optimization by adding counts of sub-combinations
    # TC = O(N)
    # SC = O(1)

    count_c = 0
    count_co = 0
    count_cow = 0

    for char in string:
        if char == "C":
            count_c += 1
        elif char == "O":
            count_co += count_c
        elif char == "W":
            count_cow += count_co

    return count_cow

# def find_possible_count(n: int, string:list[str]) -> int:
#     # Very straightforward solution
#     # TC = O(n^3)
#     # SC = O(1)
#     count = 0

#     for i in range(n):
#         if string[i] != "C":
#             continue

#         for j in range(i+1, n):
#             if string[j] != "O":
#                 continue

#             for k in range(j+1, n):
#                 if string[k] != "W":
#                     continue
                
#                 count += 1

#     return count


if __name__ =="__main__":
    # For each given character in string,
    # count the combinations of which makes 'COW'
    # Since the lengt of string n is under 100(1<=n<=100),
    # and its consisting characters only be 'C','O','W',
    # it can be solved with O(n^3) easily

    # Aside:
    # the capacity of modern systems operations per second≈10^8
    # so under the restriction of 5000ms, it can expand to 5*10^8
    # which makes the given input of length n <= (5*10^8)^(1/3) == 800
    
    # However, to reduce the TC, maybe I could use additional pointers? -> Yes
        
    n = int(input())
    string = [char for char in input()]

    print(find_possible_count(n,string))
