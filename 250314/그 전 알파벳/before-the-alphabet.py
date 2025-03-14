char = input()
order = ord(char)
prv_order = ((order - ord('a') - 1) % 26) + ord('a')

print(chr(prv_order))