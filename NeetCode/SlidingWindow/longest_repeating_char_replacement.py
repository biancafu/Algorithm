#https://leetcode.com/problems/longest-repeating-character-replacement/
# didn't know how to solve it
# neetcode solution
class Solution(object):
    def characterReplacement(self, s, k):
        seen = {}
        mostrepeat = 0
        l = 0
        maxlength = 0

        for r, char in enumerate(s):
            if char not in seen:
                seen[char] = 0
            seen[char] += 1

            mostrepeat = max(mostrepeat, seen[char]) #we don't have to update it if another number becomes the most repeated if it is still smaller than the most repeated value becuz we only want max length
            while r - l + 1 - mostrepeat > k: #size of counted string - max repeating char length = the remaining different char length
                #if remaining char length > k, we don't have enough replacement values 
                seen[s[l]] -= 1
                l += 1
            
            maxlength = max(maxlength, r - l + 1)
        
        return maxlength

