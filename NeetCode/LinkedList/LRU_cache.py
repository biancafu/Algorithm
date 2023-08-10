#21 min with very slow time 17%, don't think my solution satisfies the requirement (not sure) becuz put has min which is O(n)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.order = {}
        self.count = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.count += 1
        if key in self.cache:
            self.order[key] = self.count
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        self.count += 1
        if len(self.cache) < self.capacity or key in self.cache:
            self.cache[key] = value
            self.order[key] = self.count
        else:
            k = self.order.keys()[self.order.values().index(min(self.order.values()))]
            self.cache.pop(k)
            self.order.pop(k)
            self.order[key] = self.count
            self.cache[key] = value