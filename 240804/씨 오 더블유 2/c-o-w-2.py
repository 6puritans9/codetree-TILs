def count_COW_sequences(n, _string):
    dpC = [0] * n
    dpO = [0] * n
    dpW = [0] * n
    
    # Initialize the dpC array
    dpC[0] = 1 if _string[0] == 'C' else 0
    
    for i in range(1, n):
        dpC[i] = dpC[i - 1]
        dpO[i] = dpO[i - 1]
        dpW[i] = dpW[i - 1]
        
        if _string[i] == 'C':
            dpC[i] += 1
        elif _string[i] == 'O':
            dpO[i] += dpC[i - 1]
        elif _string[i] == 'W':
            dpW[i] += dpO[i - 1]

    return dpW[-1]

# Read input
n = int(input())
_string = input()

# Compute the number of valid 'COW' sequences
result = count_COW_sequences(n, _string)
print(result)