char = input()
order = ord(char)
nxt_order = ((order - ord('a') + 1) % 26) + ord('a')

print(chr(nxt_order))