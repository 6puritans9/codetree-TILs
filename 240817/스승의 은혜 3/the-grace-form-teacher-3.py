def max_gifts(N, B, gifts):
    gifts.sort(key=lambda x: x[0] + x[1])
    
    def count_gifts(coupon_index):
        budget = B
        count = 0
        for i, (price, shipping) in enumerate(gifts):
            cost = price + shipping
            if i == coupon_index:
                cost = price // 2 + shipping
            if budget >= cost:
                budget -= cost
                count += 1
            else:
                break
        return count

    return max(count_gifts(i) for i in range(N))

N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
gifts = [gift for gift in gifts if gift[0] % 2 == 0]  # Filter out odd prices

print(max_gifts(len(gifts), B, gifts))