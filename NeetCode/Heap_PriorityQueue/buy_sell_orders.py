import math
from heapq import heappush, heappop, heappushpop
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        '''
        order [[price, amount, orderType], [], ...]
        orderType:  0 -> buy
                    1 -> sell
        
        backlog for orders not executed (initially empty)
        buy order: look at smallest price for sell order in backlog, 
        if min sell order's price <= curr buy's price, then it will execute, and sell order will be removed from backlog.
        if min sell order's price > cur buy's price, then buy order is added to backlog

        sell order: look at largest price for buy order in backlog,
        if max buy order's price >= curr sell price, they will match and execute, buy order will be removed from backlog.
        if max buy order < curr sell price, the sell order will be added to backlog

        return total amount of orders in backlog 


        heap:
        buy order backlog -> maxheap 
        sell order backlog -> minheap

        1st approach failed, i think it still worked, but i was getting confused later on and overcomplicated things
        2nd approach:
        go through the loop, add the orders into the backlog
        then check backlog, when condition satisfies, means we can pop stuff
        easier, be sure to pay attention to details

        ** tuple is immutable, zip will combine stuff, arr1+arr2 will basically connect the 2 arrays into 1
        '''
        sell, buy = [], []
        for price, amount, order in orders:
            if order == 0:
                heappush(buy, (-price, amount))
            else:
                heappush(sell, (price, amount))
        

            while sell and buy and -buy[0][0] >= sell[0][0]:
                (sell_price, sell_amount) = heappop(sell)
                (buy_price, buy_amount) = heappop(buy)

                if sell_amount - buy_amount > 0:
                    heappush(sell, (sell_price, sell_amount - buy_amount))
                elif buy_amount - sell_amount > 0:
                    heappush(buy, (buy_price, buy_amount - sell_amount))
        


        return sum(amount for p, amount in (buy+sell)) % (10**9+7) #10**9 + 7
        