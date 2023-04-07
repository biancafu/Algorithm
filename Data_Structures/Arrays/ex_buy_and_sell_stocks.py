#Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another.

def buy_and_sell_stocks(prices):
    #my answer
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit

def solution(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stocks(A))
print(solution(A))