class Solution(object):
    def topKFrequent(self, nums, k): #O(n^2) because of max?
        #since k is gauranteed to be in the range of unique number, we don't have to check that
        #gauranteed answer is unique meaning we don't have to consider 2 numbers having same occurence?
        #use hashmap to record the frequency of each number
        #for number of k times, get the max of values of the frequency
        occurrence = dict()
        for i in nums:
            if i not in occurrence:
                occurrence[i] = 0
            occurrence[i] += 1

        frequency = occurrence.values()
        result = []
        for i in range(k):
            index = occurrence.keys()[frequency.index(max(frequency))] #finding the key of max frequency
            result.append(index) 
            frequency.remove(max(frequency)) #remove the highest frequency
            occurrence.pop(index) #remove by key
        
        return result