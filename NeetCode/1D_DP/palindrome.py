class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        palindrome: when count from left == count from right (can stop when we are at mid)
        even length: 
            mid = len(s) // 2
            left, right = s[0:mid], s[mid::][::-1]
            if left == right then true else false
            (we cannot do s[mid:end:-1] becuz this is saying starting from mid to end, step is -1, which will return nothing since theres no way for start to go to end if we are always -1 everytime)

        odd length:
            mid = len(s)//2
            left = s[0:mid]
            right = s[mid+1:][::-1] #we are skipping middle value
            if left == right then true else false

        find the longest?
        use a for loop, dfs every character except last one 
        create a dict to record down if this is pallindrome
        if the pointer already exist in dict, we will just return the answer from dict
        """

        longest = [0, 0]
        seen = {}
        
        def is_palindrome(input):
            pass
        
        def dfs(i,j):


            for i in range(len(s)):
                for j in range(i, len(s)):
                    pass
                
                
        

        return s[longest[0]:longest[1]]



        
        