 #8 min O(n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #length of both string has to be equal for than to be anagram
        if len(s) != len(t):
            return False 
        
        occurence = dict()
        for char in s:
            if char not in occurence:
                occurence[char] = 0
            occurence[char] += 1
        
        for char in t:
            if char in occurence:
                occurence[char] -= 1
                if occurence[char] == 0:
                    occurence.pop(char)
            else:
                return False
            
        #don't need this since we checked the length already (if we don't check, then we need this)
        # if len(occurence) == 0:
        #     return True
        # else:
        #     return False

# another approach:
# strings and tuples are immutable, you can't use sort() to modify them in place
# However, sorted() accepts any iterable objects, including lists, strings, and tuples, and returns a new sorted list.

        # if len(s) != len(t):
        #             return False

        #         new_s = sorted(s)
        #         new_t = sorted(t)
        #         return new_s == new_t #used a for loop initially, even slower

# This is a lot slower (~40%) than the previous solution, because sorting 2 strings = O(NlogN + MlogM)