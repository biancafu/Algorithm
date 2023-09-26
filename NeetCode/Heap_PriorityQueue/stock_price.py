import heapq
class StockPrice(object):

    """
    input: timestamp = int, price = int
    assuming prev wrong, curr correct (replace)

    initialize with:
    price = {}
    maxheap = [] #O(1) for max
    minheap = [] #O(1) for min
    latesttime = 0 #latest time stamp

    update:
    update price = price[timestamp = 1] = 3 (price)
    update maxheap, minheap
    minheap = [(price = 2, timestamp = 1), (price = 3, timestamp = 1)]
    latesttime if max(lattesttime, currtime)

    curr:
    return price[latesttime]

    min:
    minheap[0]: price = 2, timestamp = 1
    while minheap[0][0] != price[minheap[0][1]]: 
        heappop #pop the wrong answer
    
    return minheap[0][0] 


    """

    def __init__(self):
        self.price = {} #key = timestamp, value = price
        self.maxheap = [] 
        self.minheap = []
        self.latesttime = 0

        

    def update(self, timestamp, price):
        #updating price to timestamp (correcting if it exist)
        self.price[timestamp] = price
        self.latesttime = max(timestamp, self.latesttime)
        heapq.heappush(self.maxheap, (-price, timestamp))
        heapq.heappush(self.minheap, (price, timestamp))


        

    def current(self):
        #based on wht we have, find latest price (latest time stamp record of the time not enter order)
        """
        :rtype: int
        """
        return self.price[self.latesttime]
        

    def maximum(self):
        """
        :rtype: int
        """
        while -self.maxheap[0][0] != self.price[self.maxheap[0][1]]:
            heapq.heappop(self.maxheap) #pop the wrong price
        
        return -self.maxheap[0][0]
        

    def minimum(self):
        """
        :rtype: int
        """
        if not self.price:
            print("update a price first")
            return 
        while self.minheap[0][0] != self.price[self.minheap[0][1]]:
            heapq.heappop(self.minheap) #pop the wrong price
        
        return self.minheap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()