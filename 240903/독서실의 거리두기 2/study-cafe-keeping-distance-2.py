def max_min_distance(N, seats):
    # Convert the string into a list of indices where seats are occupied
    occupied = [i for i in range(N) if seats[i] == '1']
    
    max_dist = 0
    
    # Check the distance we can achieve by placing the new person at either end
    # Check at the beginning (before the first '1')
    max_dist = max(max_dist, occupied[0])
    
    # Check in between each pair of consecutive '1's
    for i in range(1, len(occupied)):
        max_dist = max(max_dist, (occupied[i] - occupied[i - 1]) // 2)
    
    # Check at the end (after the last '1')
    max_dist = max(max_dist, N - 1 - occupied[-1])
    
    return max_dist

# Read inputs
N = int(input())
seats = input().strip()

# Print the result
print(max_min_distance(N, seats))