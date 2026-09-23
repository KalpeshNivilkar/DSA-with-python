"""def bestTimeToBuyAndSellStock(prices):
    max = float('-inf')
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] - prices[i] > max:
                max = prices[j] - prices[i]
    return max if max > 0 else 0

prices = [7,1,4,5,6,3]
print(bestTimeToBuyAndSellStock(prices))"""



def best_time_to_sell_and_buy(prices):
    min_price = float('inf')
    max_price = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_price:
            max_price = prices[i] -min_price
    return max_price
prices = [7,1,4,5,6,3]
print(best_time_to_sell_and_buy(prices))