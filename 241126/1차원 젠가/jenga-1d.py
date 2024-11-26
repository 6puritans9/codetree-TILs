n = int(input())
blocks = [int(input()) for _ in range(n)]
instructions = [tuple(map(int, input().split())) for _ in range(2)]

for s, e in instructions:
    start = s - 1
    end = e
    remains = []

    blocks = blocks[:start] + blocks[end:]

print(len(blocks))
for block in blocks:
    print(block)
    