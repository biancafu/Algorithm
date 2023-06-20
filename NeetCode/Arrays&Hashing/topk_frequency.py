class Solution(object):
    def topKFrequentNeetCode(self, nums, k): #Neetcode solution, O(n) using bucket sort
        hashmap = dict()
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        #bucket sort
        #for answers not unique
        frequency = [[] for i in range(len(nums) + 1)] #k + 1 because 0 frequency won't count
        for key, count in hashmap.items():
            frequency[count].append(key) 

        result = []
        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result
    
    #not a good solution, rather sort O(nlogn)
    def topKFrequent(self, nums, k): #O(n^2) because of max and index??
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
    
