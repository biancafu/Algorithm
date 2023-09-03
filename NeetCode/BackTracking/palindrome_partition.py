#had to check solution but basically got the idea
# 94% speed 55% memory
class Solution(object):
    def partition(self, s):
        #for every character, we are checking every possibility of palindrome
        #this means we can have "a" or "aba" or "acca" in the beginning, we have to check all posibilities of palindrom with EACH character by pairing them one by one with a for loop
        #from the given startindex, we keep checking with increments of 1s, if the next combination can be a palindrome, once we find a palindrome, we add it to the array for current level, and check the next index by calling itself with index+1

        res = []
        level = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        def dfs(start):
            if start >= len(s):
                res.append(level[:])
                return
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    level.append(s[start:i+1])
                    dfs(i+1)
                    level.pop()
        
        dfs(0)
        return res





        