def parse(_string):
    indices = {
        "C" : [],
        "O" : [],
        "W": []
    }
    
    for i, char in enumerate(_string):
        indices[char].append(i)

    return indices
        

n = int(input())
_string = input()
indices = parse(_string)

count = 0
for c_idx in indices["C"]:
    for o_idx in indices["O"]:
        for w_idx in indices["W"]:
            if c_idx < o_idx < w_idx:
                count += 1

print(count)