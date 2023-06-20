#https://leetcode.com/problems/group-anagrams/
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
#default dict can have list, set, or int
#when any key, that does not exist in the defaultdict is added or accessed, it is assigned a default value as opposed to giving a KeyError
#empty key will assign empty default(set, list, or 0 for int)


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) #default value will be list for this map
        for string in strs:
            occurrence = [0] * 26 # a list of occurence of characters for this string

            for char in string:
                occurrence[ord(char) - ord("a")] += 1 #index: a = 0, b = 1...
            
            result[tuple(occurrence)].append(string) #use tuple cause list cannot be key, but tuples can since they are immutable

        return result.values()