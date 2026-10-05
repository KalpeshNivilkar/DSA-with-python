"""def bestTimeToBuyAndSellStock(prices):
    max = float('-inf')
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] - prices[i] > max:
                max = prices[j] - prices[i]
    return max if max > 0 else 0

prices = [7,1,4,5,6,3]
print(bestTimeToBuyAndSellStock(prices))"""



'''def best_time_to_sell_and_buy(prices):
    min_price = float('inf')
    max_price = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_price:
            max_price = prices[i] -min_price
    return max_price
prices = [7,1,4,5,6,3]
print(best_time_to_sell_and_buy(prices))'''


'''nput: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: Buy for price 1 and sell for price 9. '''


# Brute force approach
def buy_and_sell(nums):
    n = len(nums)
    max_profit = 0
    for i in  range(n):
      for j in range(i+1, n):
         if nums[j] > nums[i]:
            profit = nums[j] - nums[i]
            max_profit = max(profit, max_profit)
    return max_profit


        
nums = [7, 10, 1, 3, 6, 9, 2]
print(buy_and_sell(nums))

# optimal approacxh
def buy_sell_stock(nums):
    n = len(nums)
    min_num = float('inf')
    max_profit = 0

    for i in range(n):
        min_num = min(min_num, nums[i])
        max_profit = max(max_profit, nums[i] - min_num)

    return max_profit
nums = [7, 10, 1, 3, 6, 9, 2]
print(buy_sell_stock(nums))

     