string = [char for char in input().split()]
orders = [ord(char) for char in string]

result = []
result.append(orders[0] + orders[1])
result.append(abs(orders[0] - orders[1]))

print(*result, sep=" ")