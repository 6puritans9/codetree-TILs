a = list(map(int, input()))

for idx, digit in enumerate(a):
    if idx == 0:
        continue
    
    if digit == 0:
        a[idx] = 1
        break

    if idx == len(a) - 1:
        a[-1] = 0
    
deci = 0
for i, digit in enumerate(a):
    exponent = (len(a) - 1) - i

    deci += digit * 2**(exponent)

print(deci)