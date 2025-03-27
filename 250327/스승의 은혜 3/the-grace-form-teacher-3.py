def find_max_presents(n:int, b:int, presents:list[int]) -> int:
    # TC = O(N^2) = O(10^6) == 0.8s
    # SC = O(1)
    
    max_count = 0

    for i in range(n):
        budget = b
        p1, s1, t1 = presents[i]
        p1 //= 2
        count = 0
        if b >= p1 + s1:
            count += 1
        
        budget -= (p1 + s1)

        for j in range(n):
            if i == j:
                continue

            p2, s2, t2 = presents[j]
            if budget < t2:
                break
            count += 1
            budget -= t2
        
        max_count = max(max_count, count)

    return max_count


if __name__ == "__main__":
    # For N students with budget B,
    # Price(i) and Shipping(i) given for N times
    # Only one item's price can be halved
    # Find the maximum number of students that can receive presents
    
    # Constraints
    # 1 <= N <= 10^3
    # 1 <= B <= 10^3
    # 0 <= P(i), S(i) <= 10^3
    # P(i)s are even numbers
    # Time 5000ms
    # Space 288MiB

    # Approach
    # 1. Since the N <= 10^3, O(N^2) solution is feasible
    # 2. sort the presents in ascending order by P(i) + S(i): O(nlogn)
    # 3. for i in range(n):
    #       p(i) //= 2
    #       for j in range(n):
    #           if i != j:
    #               pass

    n, b = map(int, input().split())
    presents = []
    for _ in range(n):
        p, s = map(int, input().split())
        presents.append((p, s, p+s)) # price, shipping, total
    
    presents.sort(key=lambda x:x[2])
    print(find_max_presents(n, b, presents))
